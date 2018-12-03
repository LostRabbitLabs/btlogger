#!/usr/bin/expect
set command2 "exit"
spawn bluetoothctl
expect "bluetooth"
sleep 2
send "$command2\r";
interact
