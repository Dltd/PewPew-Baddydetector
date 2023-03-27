#!/usr/bin/python
# BaddyDetector v0.69
# -----------------------
# pewserver.{version}.py PoC
# .__ . ,   .
# |  \|-+- _|
# |__/| | (_]
#
# Version: v3.1
# -----------------------
# This PoC consists of a server and client script, the server listens to multiple ports,
# and the client connects to these ports. Log files are 'tailed' and will have the client
# blink a corresponding LED when the new entries arrive.
#
# The pewserver.py script listens on multiple ports, each corresponding to a specific log file.
# -----------
# When a client connects to any or all of the ports, the server tails the associated log file in real-time.
# The client script is pewclient.py.
# ------------
# For each new line detected in the log, the server sends a signal to the connected client.
# The cowrie logfile for port 54637 will only send a signal when input in the honeypot is entered.
#
# When the client disconnects, the server gracefully handles the disconnection and continues listening for new connections.
# -----------------------
#
#

# Asynchronous tasks in the asyncio module allow for concurrent execution of multiple tasks without
# blocking the main thread. The module uses an event loop to manage the execution of these tasks,
# allowing them to run concurrently and switch between each other when waiting for input/output or sleeping.

import asyncio  # Import the asyncio library for creating asynchronous tasks
import aiofiles  # Import the aiofiles library for asynchronous file I/O
from asyncio import StreamReader, StreamWriter  # Import the StreamReader and StreamWriter classes for communicating with the client

# Dictionary mapping ports to log files
LOG_FILES = {
    54631: "/data/cowrie/log/cowrie.json",
    54632: "/data/heralding/log/heralding.log",
    54633: "/data/ddospot/log/dnspot.log",
    54634: "/data/ddospot/log/ntpot.log",
    54635: "/data/honeytrap/log/honeytrap.log",
    54636: "/data/dionaea/log/dionaea.json",
    54637: "/data/cowrie/log/cowrie.json",
    54638: "/data/adbhoney/log/adbhoney.log",
    # Add more log files if needed
}

# Coroutine to tail log file and send updates to the connected client
#
# the data for port 54637 will only be used as a trigger for the client
# if there is input typed in the honeypot
async def tail_log_file(log_file, writer):
    """
    Tails a log file and sends updates to the connected client if the log entry contains "cowrie.command.input".

    Parameters:
    log_file (str): Path to the log file.
    writer (StreamWriter): StreamWriter object for communicating with the client.
    """
    async with aiofiles.open(log_file, "r") as f:
        await f.seek(0, 2)  # Move to the end of the file
        while not writer.is_closing():
            line = await f.readline()
            if line and "cowrie.command.input" in line and "54637" in log_file:
                try:
                    writer.write(b"1")  # Send the single character '1'
                    await writer.drain()
                except (ConnectionResetError, BrokenPipeError):
                    break
            elif line and "54637" not in log_file:
                try:
                    writer.write(b"1")  # Send the single character '1'
                    await writer.drain()
                except (ConnectionResetError, BrokenPipeError):
                    break
            else:
                await asyncio.sleep(0.1)  # Wait for a short period before checking again

# Coroutine to handle a new client connection
async def handle_connection(reader: StreamReader, writer: StreamWriter):
    """
    Coroutine to handle a new client connection. Sends log updates to the client for the corresponding port.

    Parameters:
    reader (StreamReader): StreamReader object for reading data from the client.
    writer (StreamWriter): StreamWriter object for writing data to the client.
    """
    addr = writer.get_extra_info("peername")
    port = writer.get_extra_info("sockname")[1]

    log_file = LOG_FILES.get(port)
#   if the log file is cowrie.json and the connected port is 54637
#
    if log_file and port == 54637 and "cowrie.json" in log_file:
        print(f"{addr} connected to port {port}. Sending hits from {log_file}...")
        try:
            await tail_log_file(log_file, writer)
        except ConnectionResetError:
            print(f"Connection lost: {addr}")
        except BrokenPipeError:
            print(f"Broken pipe error: {addr}")
    elif log_file:
        print(f"{addr} connected to port {port}. Sending hits from {log_file}...")
        try:
            await tail_log_file(log_file, writer)
        except ConnectionResetError:
            print(f"Connection lost: {addr}")
        except BrokenPipeError:
            print(f"Broken pipe error: {addr}")
    else:
        print(f"{addr} connected to unknown port {port}.")
        writer.write(b"Invalid port.\n")
        await writer.drain()

    print(f"{addr} disconnected.")
    writer.close()
    try:
        await writer.wait_closed()
    except (ConnectionResetError, BrokenPipeError):
        pass

# Main coroutine to start the server
async def main():
    """
    Main coroutine to start the server. Creates a server object for each port and starts serving clients.
    """
    server_tasks = []
    for port, log_file in LOG_FILES.items():
        server = await asyncio.start_server(handle_connection, "0.0.0.0", port)
        server_tasks.append(server)
        print(f"Listening on port {port} for log {log_file}...")

    await asyncio.gather(*(s.serve_forever() for s in server_tasks))

if __name__ == "__main__":
    try:
        asyncio.run(main())  # Run the main coroutine
    except KeyboardInterrupt:
        print("\nShutting down the server gracefully...")
