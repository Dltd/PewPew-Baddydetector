#!/bin/bash
tmux \
new-session \
'python /home/dltd/RnD/led/client_led1.py'\; \
split-window \
'python /home/dltd/RnD/led/client_led2.py'\; \
split-window -h \
'python /home/dltd/RnD/led/client_led3.py'\; \
split-window \
'python /home/dltd/RnD/led/client_led4.py'\; \
split-window \
'python /home/dltd/RnD/led/client_led5.py'\; \
select-layout even-horizontal\; \
