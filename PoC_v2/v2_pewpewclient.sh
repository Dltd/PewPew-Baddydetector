#!/bin/bash
# BaddyDetector v0.69
# -----------------------
# pewclient PoC using tmux
# .__ . ,   .
# |  \|-+- _|
# |__/| | (_]
#
# Create a new tmux session named "pewpew"
# split panes and excute script in each as defined
tmux new-session -d -s pewpew
tmux send-keys -t pewpew "python /home/dltd/attack_led1.py" Enter
tmux split-window -h -t pewpew
tmux send-keys -t pewpew "python /home/dltd/attack_led2.py" Enter
tmux split-window -v -p 75 -t pewpew
tmux send-keys -t pewpew "python /home/dltd/attack_led3.py" Enter
tmux split-window -v -p 66 -t pewpew
tmux send-keys -t pewpew "python /home/dltd/attack_led4.py" Enter
tmux split-window -v -p 50 -t pewpew
tmux send-keys -t pewpew "python /home/dltd/attack_led5.py" Enter
tmux select-pane -t pewpew:0.0
tmux split-window -v -p 75 -t pewpew
tmux send-keys -t pewpew "python /home/dltd/attack_led6.py" Enter
tmux split-window -v -p 66 -t pewpew
tmux send-keys -t pewpew "python /home/dltd/attack_led7.py" Enter
tmux split-window -v -p 50 -t pewpew
tmux send-keys -t pewpew "python /home/dltd/attack_led8.py" Enter
##########################
# Run something in all 8 panes at once
# Set pane sync
#tmux set-window-option -t pewpew:0 synchronize-panes on
#
#tmux send-keys -t pewpew "date" Enter
#
# Attach to session named "pewpew"
##########################
# want to connect to the tmux session?
#tmux attach -t pewpew
