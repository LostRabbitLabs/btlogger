# btlogger.py

B L U E T O O T H  ::::  L O G G E R - v1.0<BR>
Bluetooth Logger, Plotter and De-Mystifier!<BR><BR>
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-<BR>
INSTALL/PRE-REQS:<BR>
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-<BR>
1. Install python:<BR>
apt-get install python

2. Install pip!<BR>
apt-get install python-pip
pip install --upgrade pip

3. Install needed Python libs:<BR>
- apt-get install screen<BR>
- apt-get install expect<BR>
- pip install matplotlib<BR>
- pip install pandas<BR>

<BR>
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-<BR>
INSTALLING:<br>
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-<BR>

Install 'btlogger' into /opt:<BR>

GIT CLONE the 'btlogger' script/framework:<BR>
cd /opt<BR>
git clone https://github.com/LostRabbitLabs/btlogger<BR>
cd btlogger<BR>
<BR><BR>

Update "inc/run-reports.sh" with your correct BLUETOOTH MAC ADDRESS:<BR>

## CHANGE MAC ADDRESS BELOW  VVVVVVV
cd /var/lib/bluetooth/01:02:03:AB:CD:DE/cache ; /usr/bin/tail -n +1 * > /opt/btlogger/BT-devices.txt

<BR><BR>
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-<BR>
HOW TO USE:<BR>
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-<BR>

Usage:<BR>
1. Run "sh /opt/btlogger/btlogger-v1.sh" to generate logs<BR>

2. Run "sh /opt/btlogger/inc/run-reports.sh" to generate report data (shows up in /opt/btlogger directory)<BR>

3. Optionally, add the lines below to your /etc/crontab file for persistence:<BR>
*/15 * * * * root sh /opt/btlogger/inc/restart-services.sh<BR>
*/5 * * * * root sh /opt/btlogger/inc/run-reports.sh<BR>

<BR>

-theLostRabbit
<BR>


