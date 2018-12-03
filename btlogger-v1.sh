#!/bin/bash
/usr/bin/touch /opt/btlogger/BT-LOG.txt
cd /opt/btlogger/inc ; /usr/bin/screen -S BTLOGGER -dm -c /bin/bash /opt/btlogger/inc/run-expect.sh > /dev/null
sleep 3
cd /opt/btlogger ; /opt/btlogger/inc/btlog2csv.py & >/dev/null 2>&1

