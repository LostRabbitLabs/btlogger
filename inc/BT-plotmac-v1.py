#!/usr/bin/python
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as md
import pandas as pd
import sys

macaddr = sys.argv[1]

try:
    dg1 = pd.read_csv('/opt/btlogger/BT-LOG.csv', header=0, index_col=0, parse_dates=True, sep=';',usecols=[0,1], names=['stamp','mac'])
    df1 = pd.read_csv('/opt/btlogger/BT-LOG.csv', header=0, sep=';',usecols=[0,1,2], names=['stamp','mac','vendor'])
    df2 = df1[df1.mac==macaddr]
    dg2 = dg1[dg1.mac==macaddr]
except:
    print "major error in pd.read_csv !!!!!"


try:
    total_dates = len(df2['stamp']) - 1
    if total_dates == 0:
        total_dates = 1
    total_macs = len(dg2['mac']) - 1
    if total_macs == 0:
        total_macs = 1
except:
    pass
    print "error getting total macs/dates !!!!"


begin1 = []
end1 = []
vendors = []

a = 0

while a < total_dates:
    try:
        newstamp = df2.stamp.iloc[a]
        newvendor = df2.vendor.iloc[a]
        time1 = datetime.datetime.strptime(newstamp, '%Y-%m-%d %H:%M:%S')
        begin1.append(time1)
        vendors.append(newvendor)
        a = a + 1
    except:
        pass
        print "error looping thru newstamp/vendors !!!!"
        a = a + 1


total_bts = len(begin1)
y = [1] * total_bts

##testing
x = begin1

end_time  = datetime.datetime.now()
#start_time = end_time - datetime.timedelta(minutes=5)
start_time = df1.stamp[0]
#start_time = datetime.datetime.now() - datetime.timedelta(minutes=5)


try:
    fig, ax = plt.subplots()
    #ax.plot_date(x, y, markerfacecolor='CornflowerBlue', markeredgecolor='white')
    ax.plot_date(x, y, markerfacecolor='Pink', markeredgecolor='Red', markersize=10, marker='o',)
    fig.autofmt_xdate()
    #new code
    ax.fmt_xdata = md.DateFormatter('%Y-%m-%d %H:%M:%S')
    ax.xaxis.set_major_formatter(md.DateFormatter('%Y-%m-%d %H:%M:%S'))
    ax.grid(True)
    ax.set_xlim([start_time, end_time])
    ax.set_ylim([0, 5])
    total_macs_str = str(total_macs)
    macaddrfull = macaddr + "\n" + newvendor + " = " + total_macs_str
    ax.set_yticklabels(['', macaddrfull])
    plt.tight_layout()
except:
    pass
    print "ax.plotting functions error !!!!"

try:
    outputfile = "/opt/btlogger/plots/" + macaddr+".png"
    plt.savefig(outputfile)
except:
    pass
    print "error saving outputfile !!!!"

sys.exit()


