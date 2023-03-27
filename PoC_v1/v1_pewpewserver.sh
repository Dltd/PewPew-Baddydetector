#!/bin/bash
tmux \
new-session \
'tail -f /data/cowrie/log/cowrie.json | nc -kvklp 54635'\; \
split-window \
'tail -f  /data/heralding/log/heralding.log | nc -nvklp 54634'\; \
split-window -h \
'tail -f /data/cowrie/log/cowrie.json | grep "cowrie.session.connect" | nc -nvklp 54633'\; \
split-window \
'tail -f /data/ddospot/log/dnspot.log | nc -nvlkp 54632'\; \
split-window \
'tail -f /data/cowrie/log/cowrie.json | grep "cowrie.command.input" | nc -nvklp 54631'\; \
select-layout even-horizontal\; \
