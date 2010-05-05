#!/bin/bash

PID=$(ps aux | grep beaglebot.py | grep python | grep -v grep | awk '{print $2}')

for MYPID in $PID;
do
	kill $PID
done
