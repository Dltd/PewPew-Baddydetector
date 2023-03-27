# Some details of the build

The stl file used to print the LED stand [can be found here](/PoC_v1/PewPewBaddyDetectorV1.stl).
It was not made with beauty in mind, so the quality might not be all too good ;)

The TinkerCAD 3D file can be found [here](https://www.tinkercad.com/things/1tUUNth2Pv8).

# v1 model
https://youtube.com/shorts/qewCp_70Njc


<img src="/PoC_v1/v1_first_model_led.JPEG" width="40%" height="40%" />



# POC v1
<img src="img/PoCv1.gif"/>

Using a really simple setup with nc, tail and tmux was the quickest way to test my initial idea which works fine for the PoC.

The server script runs on a Linux server that runs a collection of honeypots, [T-Sec's TPOTCE](https://github.com/telekom-security/tpotce).

The /data directory contains the logs of the different honeypots, I selected a few popular pots to use for my idea.
The idea is for a similar but larger project and needed this PoC to get it going.

I wanted to create a physical dashboard that would notify me when there was an attack taking place on one of the honeypots.
Since this does not require a lot of power, I decided to use a Raspberry Pi 1 that I had lying around.

The RPi as a client will connect to specified ports on the server, where the server script runs.
I designed and printed a small LED holder that could stand on my desk and wired the LEDS to the RPi.

The server script will create 5 panes and run the relevant commands:

[v1_pewpewserver.sh](/PoC_v1/v1_pewpewserver.sh)

The client script will create 5 panes and run a python script that blinks a LED when an new entry arrives in the honeypot logs:

[v1_pewpewclient.sh](/PoC_v1/v1_pewpewclient.sh)

The pyton script "client_led{num}.py" is used to blink 1 LED, multiple scripts are used in this test: 

[v1_client_led1.py](/PoC_v1/v1_client_led1.py)
