#!/usr/bin/expect
set command1 "scan on" 
spawn bluetoothctl
expect "bluetooth"
send "$command1\r";
interact
