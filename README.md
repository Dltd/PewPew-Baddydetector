# Baddydetector
PoC for having actions of baddies in the virtual world, visible in the physical world.

v3:
The Raspberry Pi connects to a server on which multiple honeypots run.
The server listens on 8 ports and will monitor the log files of the honeypots for new attacks or automated scans and hacking attempts. 

The logs are tailed and bound to one of the ports. One log is monitored twice, where the second time it is filtered on a keyword.
When the keyword is detected, it reflects input being entered in a shell on one of the honeypots. The connected LED only blinks when a bot or person actually does something in the pot.

When an activity takes place on the selected honeypots, the server will send a '1' to the client, the RPi.

When the client receives the data, it will blink two LEDs which are connected to the GPIO pin per port. 8 GPIO's are used to blink the 16 leds. 

The honeypot configuration will be deciding in if 'innocent' traffic will also be registered and blink a LED or not.
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

# PoC v3
[![name](/img/PoCv3.gif)](/PoC_v3/)
  
# PoC v2
[![name](/img/PoCv2.gif)](/PoC_v2/)

# PoC v1
[![name](/img/PoCv1.gif)](/PoC_v1/)

