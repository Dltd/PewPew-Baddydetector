# Baddydetector
PoC for having actions of baddies in the virtual world, visible in the physical world.

![Version 3](/PoC_v3/img/v3.JPG)

# Pics
[some of the 3D stuff](https://github.com/Dltd/PewPew-Baddydetector/blob/main/PoC_v3/README.md#3d-stuff)

[Mess is fun!](https://github.com/Dltd/PewPew-Baddydetector/blob/main/PoC_v3/README.md#some-mess)

[Soldering and wiring](https://github.com/Dltd/PewPew-Baddydetector/blob/main/PoC_v3/README.md#soldering-and-wiring)

# v3
The Raspberry Pi connects to a server on which multiple honeypots run.
The server listens on 8 ports and will monitor log files of 8 honeypots for new attacks or automated scans and hacking attempts. 

The logs are tailed and bound to one of the ports. One log is monitored twice, where the second time it is filtered on a keyword.
When the keyword is detected, it reflects input being entered in a shell on one of the honeypots. The connected LED only blinks when a bot or person actually does something in the pot.

When an activity takes place on the selected honeypots, the server will send a '1' to the client, the RPi.

When the client receives the data, it will blink two LEDs which are connected to the GPIO pin per port. 8 GPIO's are used to blink the 16 leds. 

The honeypot configuration will be decisive if 'innocent' traffic will also be registered and blink a LED or not.
As this is not yet the final version of the idea I have, that will be for later to further tweak and tune or improve somehow.

The LEDs are put in a specific order which I liked, like so:
```bash
2	3	4	5	6	7	8
1						1
8	7	6	5	4	3	2
```

Initially I only needed to see v1 work but sometimes you just get carried away, so there you go.

For more details, consult the different versions:

[PoC_v3](/PoC_v3)

[PoC_v2](/PoC_v2)

[PoC_v1](/PoC_v1)

For the LEDs I added two test scripts to run and check if you have any dead LEDs.
You can find them [here](/Other_scripts/)


# Some details of the build

The stl file used to print it [can be found here](/PoC_v3/PewPewBaddyDetectorV3.stl)

note: The LED holes might need manual adjustment to make them fit properly.
The design is for 5mm LED's.

You can edit it yourself on TinkerCAD [here](https://www.tinkercad.com/things/2NkG0boZJYC)

The server script runs on a Linux server that runs a collection of honeypots, [TPOT-CE](https://github.com/telekom-security/tpotce).
The /data directory contains the logs of the different honeypots, I selected a few popular pots to use for my idea.
The idea is for a similar but larger project and it needed this PoC to get it going.

I wanted to create a physical dashboard that would notify me when there was an attack taking place on one of the honeypots.
Since this does not require a lot of power, I decided to use a Raspberry Pi 1 that I had lying around.

The RPi as a client will connect to specified ports on the server running the server script.
I designed and printed a LED holder that could stand on my desk and wired the LEDS to the RPi.

I have done some undocumented tests with a RPi Zero W but the functionality is limited due to the lack of real threading.
This can be simulated and runs sort of near real time but I haven't had time to further explore it yet.


# v3 model
https://youtu.be/B9omcdxjBJs

![](/img/aLottaVaPewa.gif)

# PoC v3

[![v3BaddyDetector](/img/PoCv3.gif)](https://www.youtube.com/watch?v=B9omcdxjBJsQ)

[Server](/PoC_v3/v3_pewserver.v3.1.py)

[Client](/PoC_v3/v3_pewclient.v3.py)


To make it more useful and easier to maintain, the v2 functionality was converted to python.

# PewClient and PewServer

Two Python scripts, pewclient.py and pewserver.py are designed to work together to monitor log files and visually indicate new attacks using LEDs on a Raspberry Pi.

# PewClient

The pewclient.py script runs on a Raspberry Pi 1 that I had lying around, collection dust. It is responsible for connecting to the pewserver.py script. Upon receiving signals from the server, it blinks the corresponding LED to indicate new attacks taking plsce. The script automatically reconnects to the server if the connection is lost and can be gracefully terminated by typing exit in the console. 

# PewServer

The pewserver.py script is a server that listens on multiple ports, each corresponding to a specific log file. When a client (like pewclient.py) connects to one of the ports, the server tails the associated log file in real-time. For each new line detected in the log, the server sends a signal to the connected client.

For one log, the data is filtered to reflect current activitiy by a bot or baddie in a shell in one of the honeypots.

When the client disconnects, the server gracefully handles the disconnection and continues listening for new connections.

# Setup

Clone the repository:
```bash
git clone https://github.com/Dltd/PewPew-Baddydetector.git
```

Update the IP address and port numbers in both pewclient.py and pewserver.py to match your configuration.

Make sure the required dependencies are installed on the RPi and the server running the server script:

RPi:
```bash
pip install gpiozero aioconsole asyncio
```
Server:
```bash
pip install asyncio aiofiles
```

# Running the PoC

Run the pewserver.py script on the machine where the log files are located:
```bash
python3 pewserver.py
```

Run the pewclient.py script on the Raspberry Pi connected to the LEDs:
```bash
python3 pewclient.py
```

# Usage
When the pewclient.py script is running and connected to the pewserver.py script, it will blink the LEDs according to the incoming signals from the server. Each LED corresponds to a specific log file, and blinks whenever there is a new entry in that log file.

To gracefully stop the pewclient.py script, type exit in the console.

The LEDs are wired in pairs, in my PoC I used this configuration to make it more fun.

```
2	3	4	5	6	7	8

1						1

8	7	6	5	4	3	2
```



#  3D stuff

<img src="/PoC_v3/img/v3-3D%20(1).JPEG" width="40%" height="40%" />

<img src="/PoC_v3/img/v3-3D%20(2).JPEG" width="40%" height="40%" />

<img src="/PoC_v3/img/v3-3D%20(3).JPEG" width="40%" height="40%" />

<img src="/PoC_v3/img/v3-3D%20(4).JPEG" width="40%" height="40%" />

# Some mess
<img src="/PoC_v3/img/v3-in-the-making%20(1).JPEG" width="40%" height="40%" />

<img src="/PoC_v3/img/v3-in-the-making%20(1).jpg" width="40%" height="40%" />


<img src="/PoC_v3/img/v3-mess%20(1).JPEG" width="40%" height="40%" />

<img src="/PoC_v3/img/v3-mess%20(1).jpg" width="40%" height="40%" />

<img src="/PoC_v3/img/v3-mess%20(2).JPEG" width="40%" height="40%" />

# Soldering and wiring

Initially I had the LEDs soldered to a prototyping board.

The print I made and the base holding the print required some tweaking and tuning but since it was "just" for a PoC I didn't give it the extra bit of TLC it needed to make it fit properly. Also, the board was just a little too big to have space left to get the leds into the holes. 

So, I used a soldering iron to melt away some of the excess filament of the "neck" of the base but that did not improve that challenge all that much. ALso the center bottom three leds cannot be pushed in deep enough.

After soldering them all on the board, I cut them loose again and soldered wires on to the leds to have a little bit more freedom of movement within the casing.

<img src="/PoC_v3/t725.png" width="40%" height="40%" />

<img src="/PoC_v3/img/v3-wiring-and-leds%20(1).JPEG" width="40%" height="40%" />

<img src="/PoC_v3/img/v3-wiring-and-leds%20(2).JPEG" width="40%" height="40%" />

<img src="/PoC_v3/img/v3-wiring-and-leds%20(3).JPEG" width="40%" height="40%" />

<img src="/PoC_v3/img/v3-wiring-and-leds%20(4).JPEG" width="40%" height="40%" />

<img src="/PoC_v3/img/v3-wiring-and-leds%20(5).JPEG" width="40%" height="40%" />

<img src="/PoC_v3/img/v3-wiring-and-leds%20(6).JPEG" width="40%" height="40%" />

<img src="/PoC_v3/img/v3-wiring-and-leds%20(7).JPEG" width="40%" height="40%" />

<img src="/PoC_v3/img/v3-wiring-and-leds%20(8).JPEG" width="40%" height="40%" />

<img src="/PoC_v3/img/v3-wiring-and-leds%20(9).JPEG" width="40%" height="40%" />

<img src="/PoC_v3/img/v3-wiring-and-leds%20(10).JPEG" width="40%" height="40%" />

<img src="/PoC_v3/img/v3-wiring-and-leds%20(11).JPEG" width="40%" height="40%" />

<img src="/PoC_v3/img/v3-wiring-and-leds%20(12).JPG" width="40%" height="40%" />
