#!/bin/bash
## CHANGE MAC ADDRESS BELOW  VVVVVVV
cd /var/lib/bluetooth/01:02:03:AB:CD:DE/cache ; /usr/bin/tail -n +1 * > /opt/btlogger/BT-devices.txt
cd /opt/btlogger/inc ; ./BT-stats-v1.py /opt/btlogger/BT-LOG.csv > /opt/btlogger/BT-stats.txt &
cd /opt/btlogger/inc ; ./BT-ALL-v1.py &
cd /opt/btlogger/inc ; ./BT-LAST5-v1.py &
cd /opt/btlogger/inc ; ./BT-plotallmacs-v1.py &
cd /opt/btlogger/inc ; ./get-devices.sh > /opt/btlogger/BT-devices-5min.txt &
