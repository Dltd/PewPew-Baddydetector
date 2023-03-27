# Some details of the build

The stl file used to print the cover [can be found here](/PoC_v2/PewPewBaddyDetectorV2cover.stl)
and the base [here](/PoC_v2/PewPewBaddyDetectorV2base.stl)


The TinkerCAD 3D files can be found [here](https://www.tinkercad.com/things/a0UG9sc6krN).
and the base [is this one](https://www.tinkercad.com/things/4kdzSC4dGDb).

The server script runs on a Linux server that runs a collection of honeypots, [TPOT-CE](https://github.com/telekom-security/tpotce).
The /data directory contains the logs of the different honeypots, I selected a few popular pots to use for my idea.
The idea is for a similar but larger project and it needed this PoC to get it going.

I wanted to create a physical dashboard that would notify me when there was an attack taking place on one of the honeypots.
Since this does not require a lot of power, I decided to use a Raspberry Pi 1 that I had lying around.

The RPi as a client will connect to specified ports on the server, where the server script runs.
I designed and printed a LED holder that could stand on my desk and wired the LEDS to the RPi.

# v2 model
https://www.youtube.com/shorts/phfXufrK0ew

# Pewpew
https://youtube.com/shorts/jz_PYNGq8H0

This version works similar as v1 with bash scripts using tmux and a python script per GPIO/LED, it has a few more LEDs and a different casing.

# PoC v2

<img src="/img/PoCv2.gif"/>

[Server](/PoC_v2/v2_pewpewserver.sh)

[Client](/PoC_v2/v2_pewpewclient.sh)

[LED](/PoC_v2/v2_attackled.py)

v2 of this Proof of Concept (PoC) script  utilizes Tmux to create a new session and run multiple Python scripts concurrently in separate panes. Each script represents an individual LED on the pewclient, which blinks according to the incoming signals.

Two scripts, pewpewclient.sh and pewpewserver.sh, work together to monitor log file activity and visually indicate an attack taking place on the honeypot.
The heavily rely on ``tmux`` which is a requirement to run the scripts.

Usage
The client script creates a new Tmux session named "pewpew" and splits it into multiple panes. In each pane, it runs one of the Python scripts (attack_led1.py to attack_led8.py). These scripts control the LEDs on the pewclient, with each LED corresponding to a specific log file.

The server script creates a new Tmux session named "pewpew" and splits it into multiple panes. In each pane, it simply runs a command in each pane, similar to this:
```bash
tail -f /data/cowrie/log/cowrie.json | nc -nvklp 54631
```

A total of 8 ports will be listening and when the client connects, it will stream the data of 8 different logs to the client.
Each new entry in the log files will trigger the client script to execute the attack_led.py script to blink the appropriate led.


To connect to the Tmux session after running the script, use the following command:

```bash
tmux attach -t pewpew
```
The Tmux session helps you monitor the blinking pattern of the LEDs, allowing you to efficiently keep track of your logs in real-time.





# Some images

<img src="/PoC_v2/BaddyDetectorv2.jpg" width="40%" height="40%" />

<img src="/PoC_v2/BaddyDetectorv2cover.jpg" width="40%" height="40%" />

# Assembly

<img src="/PoC_v2/IMG_8413.JPEG" width="40%" height="40%" />

<img src="/PoC_v2/IMG_8414.JPEG" width="40%" height="40%" />

<img src="/PoC_v2/IMG_8415.JPEG" width="40%" height="40%" />

<img src="/PoC_v2/IMG_8417.JPEG" width="40%" height="40%" />

<img src="/PoC_v2/IMG_8428.JPEG" width="40%" height="40%" />

<img src="/PoC_v2/IMG_8429.JPEG" width="40%" height="40%" />

<img src="/PoC_v2/IMG_8448.JPEG" width="40%" height="40%" />

<img src="/PoC_v2/IMG_8478.JPG" width="40%" height="40%" />
