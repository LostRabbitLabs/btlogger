#!/bin/bash
pkill -9 run-expect
pkill -9 btlog2csv
sh /opt/btlogger/btlogger-v1.sh &
