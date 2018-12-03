#!/usr/bin/python
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as md
import pandas as pd
import sys
from collections import Counter
import subprocess

mac_cache = {}

#macaddr = sys.argv[1]

try:
    dg1 = pd.read_csv('/opt/btlogger/BT-LOG.csv', header=0, index_col=0, parse_dates=True, sep=';',usecols=[0,1], names=['stamp','mac'])
    df1 = pd.read_csv('/opt/btlogger/BT-LOG.csv', header=0, sep=';',usecols=[0,1,2], names=['stamp','mac','vendor'])
    unique_macs = dg1.mac.unique()
    total_umacs = len(unique_macs)
    all_macs = dg1.mac
    mac_counts = Counter(all_macs)
    mac_counts_str = str(mac_counts)
except:
    print "major error !! shitty!!!!"


top10macs = []
top10vendors = []
top10counts = []

top10 = 0


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
        print "error mac_lookup() !!!!"
        vendorname = "0"
    return vendorname



try:
    while top10 < 10:
        for macs in mac_counts:
             macs = mac_counts.most_common()[top10]
             top10macs.append(macs[0])
             top10counts.append(macs[1])
             print macs
             top10 = top10 + 1
             if top10 == 10:
                 a = 1/0
except:
    pass


try:
    end_time  = datetime.datetime.now()
    start_time = df1.stamp[0]
    start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    fig, ax = plt.subplots()
    ax.fmt_xdata = md.DateFormatter('%Y-%m-%d %H:%M:%S')
    ax.xaxis.set_major_formatter(md.DateFormatter('%Y-%m-%d %H:%M:%S'))
except:
    pass
    print "error ax.setup !!!!"

try:
    top10counts1_str = str(top10counts[0])
    top10counts2_str = str(top10counts[1])
    top10counts3_str = str(top10counts[2])
    top10counts4_str = str(top10counts[3])
    top10counts5_str = str(top10counts[4])
    top10counts6_str = str(top10counts[5])
    top10counts7_str = str(top10counts[6])
    top10counts8_str = str(top10counts[7])
    top10counts9_str = str(top10counts[8])
    top10counts10_str = str(top10counts[9])
except:
    pass
    print "error top10counts to str error !!!!"


##############################################

top10macsvendors = []

for macaddr in top10macs:
    try:
        mac_lookup(macaddr)
        #print vendorname + "!"
        newmacname = macaddr + "\n" + "(" + vendorname + ")"
        print newmacname
        top10macsvendors.append(newmacname)
    except:
        pass
        print "error macaddr in top10macs loop error!!!!"


try:
    result1 = top10macsvendors[0] + " " +  top10counts1_str
    result2 = top10macsvendors[1] + " " +  top10counts2_str
    result3 = top10macsvendors[2] + " " +  top10counts3_str
    result4 = top10macsvendors[3] + " " +  top10counts4_str
    result5 = top10macsvendors[4] + " " +  top10counts5_str
    result6 = top10macsvendors[5] + " " +  top10counts6_str
    result7 = top10macsvendors[6] + " " +  top10counts7_str
    result8 = top10macsvendors[7] + " " +  top10counts8_str
    result9 = top10macsvendors[8] + " " +  top10counts9_str
    result10 = top10macsvendors[9] + " " +  top10counts10_str
except:
    pass
    print "error result1-10 setup!!!!"


try:
    ax.set_yticks([0,1,2,3,4,5,6,7,8,9,10])
    ax.set_yticklabels(['', result1, result2, result3, result4, result5, result6, result7, result8, result9, result10])
    ax.set_ylim([0, 10])
    ax.grid(True)
    ax.set_xlim([start_time, end_time])
except:
    pass
    print "error ax.set ticks setup !!!!!"


y_index = 1

for macs in top10macs:
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
        #new code
        #ax.fmt_xdata = md.DateFormatter('%Y-%m-%d %H:%M:%S')
        #ax.xaxis.set_major_formatter(md.DateFormatter('%Y-%m-%d %H:%M:%S'))
        ##########
        #ax.set_xlim([datetime.datetime(2017, 9, 11, 19, 0, 0), end_time])
        #ax.set_yticklabels(['', macaddr])
        #macaddrfull = macs + "\n" + newvendor
        y_index = y_index + 1
        plt.tight_layout()
    except:
        pass
        print "error macs in top10 loop !!!!"


###################################################################
#plt.tight_layout()

#outputfile = "plots/" + macs[0]+".png"

try:
    outputfile = "/opt/btlogger/BT-ALL-TOP10.png"
    plt.savefig(outputfile)
except:
    pass
    print "error saving outputfile!!!!"


sys.exit()


