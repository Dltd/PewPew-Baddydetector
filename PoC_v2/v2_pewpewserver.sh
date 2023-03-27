#!/bin/bash
# BaddyDetector v0.69
# -----------------------
# pewserver PoC using tmux
# .__ . ,   .
# |  \|-+- _|
# |__/| | (_]
#
# Create a new tmux session named "pewpew"
# split panes and
# excute script in each as defined
#
# for nc, the -k switch is used on the server side to keep
# the connection open when the client has disconnected
tmux new-session -d -s pewpew
tmux send-keys -t pewpew "tail -f /data/cowrie/log/cowrie.json | nc -nvklp 54631" Enter
tmux split-window -h -t pewpew
tmux send-keys -t pewpew "tail -f  /data/heralding/log/heralding.log | nc -nvklp 54632" Enter
tmux split-window -v -p 75 -t pewpew
tmux send-keys -t pewpew "tail -f /data/ddospot/log/dnspot.log | nc -nvklp 54633" Enter
tmux split-window -v -p 66 -t pewpew
tmux send-keys -t pewpew "tail -f /data/ddospot/log/ntpot.log | nc -nvklp 54634" Enter
tmux split-window -v -p 50 -t pewpew
tmux send-keys -t pewpew "tail -f /data/honeytrap/log/honeytrap.log | nc -nvklp 54635" Enter
tmux select-pane -t pewpew:0.0
tmux split-window -v -p 75 -t pewpew
tmux send-keys -t pewpew "tail -f /data/adbhoney/log/adbhoney.log | nc -nvklp 54636" Enter
tmux split-window -v -p 66 -t pewpew
tmux send-keys -t pewpew "tail -f /data/dionaea/log/dionaea.json | nc -nvklp 54637" Enter
tmux split-window -v -p 50 -t pewpew
tmux send-keys -t pewpew "tail -f /data/cowrie/log/cowrie.json | grep "cowrie.command.input" | nc -nvklp 54638" Enter
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

