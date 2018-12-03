#!/usr/bin/python
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as md
import pandas as pd
import sys
import datetime
import sys
import os
import subprocess

try:
    dg1 = pd.read_csv('/opt/btlogger/BT-LOG.csv', header=0, index_col=0, parse_dates=True, sep=';',usecols=[0,1], names=['stamp','mac'])
    df1 = pd.read_csv('/opt/btlogger/BT-LOG.csv', header=0, sep=';',usecols=[0,1,2], names=['stamp','mac','vendor'])
    #df2 = df1[df1.mac==macaddr]
    #dg2 = dg1[dg1.mac==macaddr]
    unique_macs = dg1.mac.unique()
    total_umacs = len(unique_macs)
    all_macs = dg1.mac
except:
    print " major error pd.read_csv !!!!!"


umacs = []

try:
    with open ("/opt/btlogger/BT-unique_macs-v1.txt", "w") as outputfile:
        for macs in unique_macs:
            macs = str(macs)
            outputfile.write(macs)
            outputfile.write("\n")
except:
    pass
    print "error writing BT-unique-macs !!!!"


try:
    input_filename1 = "/opt/btlogger/BT-unique_macs-v1.txt"
    inputfile = open(input_filename1, "r")
    inputfile_data = inputfile.readlines()
    inputfile.close()
except:
    pass
    print "error opening BT-unique-macs !!!!"



def send2plot(lines):
    try:
        lines = lines.strip()
        process = subprocess.Popen("/opt/btlogger/inc/BT-plotmac-v1.py " + '"' + lines + '"' + " &",
                     shell=True,
                     stdout=subprocess.PIPE,
                   )
        asdf = str(process.communicate())
    except:
        pass


for lines in inputfile_data:
    try:
        send2plot(lines)
    except:
        pass
        print "error send2plot !!!!"


sys.exit()


