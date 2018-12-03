#!/usr/bin/python
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as md
import pandas as pd
import sys
from collections import Counter
import time
import subprocess

mac_cache = {}

#macaddr = sys.argv[1]

try:
    dg1 = pd.read_csv('/opt/btlogger/BT-LOG.csv', header=0, index_col=0, parse_dates=True, sep=';',usecols=[0,1,2], names=['stamp','mac','vendor'])
    df1 = pd.read_csv('/opt/btlogger/BT-LOG.csv', header=0, sep=';',usecols=[0,1,2], names=['stamp','mac','vendor'])
except:
    pass
    print "!!! 1-error-pd.read_csv !!!"


now1  = int(time.time())
past5minutes1  = int(time.time()-1000)

now = datetime.datetime.fromtimestamp(now1).strftime('%Y-%m-%d %H:%M:%S')
past5minutes = datetime.datetime.fromtimestamp(past5minutes1).strftime('%Y-%m-%d %H:%M:%S')

end_time  = datetime.datetime.now().replace(microsecond=0)
start_time = datetime.datetime.fromtimestamp(past5minutes1)

fivemin = dg1.loc[pd.IndexSlice[past5minutes:now,['stamp','mac','vendor']]]

top5macs = []
top5vendors = []
top5counts = []

top5 = 0

unique_macs = fivemin.mac.unique()

def mac_lookup(macaddr):
    try:
        global vendorname
        macaddr = macaddr.strip()
        if len(macaddr) > 17:
            macaddr2 = macaddr[-17:] 
            macaddr2 = macaddr2[0:8]
        else:
            macaddr2= macaddr[0:8]
        macaddr = macaddr2.replace(":","-")
        if macaddr != "":
            if macaddr in mac_cache:
                #print "macaddr is cached!\n"
                vendorname = mac_cache.get(macaddr)
            else:
                #print "no mac_cache entry\n"
                process = subprocess.Popen("cat /opt/btlogger/inc/oui.txt | grep " + '"' + macaddr + '"',
                         shell=True,
                         stdout=subprocess.PIPE,
                       )
        vendorname1 = str(process.communicate()[0].split('\n'))
        if vendorname1 != "['']":
            vendorname2 = vendorname1.split("\\t")
            vendorname3 = vendorname2[2]
            vendorname4 = vendorname3.split("\\r")
            vendorname = vendorname4[0]
        else:
            vendorname = "UNKNOWN VENDOR"
    except:
        pass
        print "error def mac_lookup() !!!!"
        vendorname = "0"
    return vendorname


try:
    while top5 < 10:
        for macs in unique_macs:
             top5macs.append(macs)
             #top5counts.append(macs[1])
             print macs
             top5 = top5 + 1
             if top5 == 10:
                #throw exception!! >;P
                 a = 1/0
except:
    pass
    print " error top10 loop !!!!"

##### new code below
fig, ax = plt.subplots()
ax.fmt_xdata = md.DateFormatter('%Y-%m-%d %H:%M:%S')
ax.xaxis.set_major_formatter(md.DateFormatter('%Y-%m-%d %H:%M:%S'))

top10macsvendors = []

for macaddr in top5macs:
    mac_lookup(macaddr)
    #print vendorname + "!"
    try:
        newmacname = macaddr + "\n" + "(" + vendorname + ")"
        print newmacname
        top10macsvendors.append(newmacname)
    except:
        pass
        print "!!!! error for macaddr in top5macs !!!!!"

try:
    result1 = top10macsvendors[0]
    result2 = top10macsvendors[1]
    result3 = top10macsvendors[2]
    result4 = top10macsvendors[3]
    result5 = top10macsvendors[4]
    result6 = top10macsvendors[5]
    result7 = top10macsvendors[6]
    result8 = top10macsvendors[7]
    result9 = top10macsvendors[8]
    result10 = top10macsvendors[9]
except:
    pass
    print "result1-10 error top10macsvendors !!!!!"

try:
    ax.set_yticks([0,1,2,3,4,5,6,7,8,9,10])
    ax.set_yticklabels(['', result1, result2, result3, result4, result5, result6, result7, result8, result9, result10])
    ax.set_ylim([0, 10])
    ax.grid(True)
    ax.set_xlim([start_time, end_time])
except:
    pass
    print "err on ax.set ticks yo !!!!"

#y_index = 1
y_index = 1

for macs in top5macs:
    try:
        df2 = df1[df1.mac==macs]
        dg2 = dg1[dg1.mac==macs]
        totals = len(df2['mac'])
        total_dates = totals
        total_macs = totals
        total_vendors = totals
        print total_dates
        print total_macs
        print total_vendors
        begin1 = []
        end1 = []
        vendors = []
        newvendors = []
        a = 0
        while a < total_dates:
            newstamp = df2.stamp.iloc[a]
            newvendor = df2.vendor.iloc[a]
            time1 = datetime.datetime.strptime(newstamp, '%Y-%m-%d %H:%M:%S')
            begin1.append(time1)
            vendors.append(newvendor)
            a = a + 1
        total_bts = len(begin1)
        y = [y_index] * total_bts
        x = begin1
        #ax.plot_date(x, y, markerfacecolor='CornflowerBlue', markeredgecolor='white')
        ax.plot_date(x, y, markerfacecolor='Pink', markeredgecolor='Red', markersize=10, marker='o',)
        fig.autofmt_xdate()
        y_index = y_index + 1
        plt.tight_layout()
    except:
        pass
        print "error for macs in top10 error!!!!"


###################################################################
#plt.tight_layout()
#outputfile = "plots/" + macs[0]+".png"

try:
    outputfile = "/opt/btlogger/BT-LAST5MIN-TOP10.png"
    plt.savefig(outputfile)
except:
    pass
    print "error saving outputfile!!!!"


sys.exit()


