#!/usr/bin/python
import sys
import subprocess
import shlex
import re
from collections import Counter

input_filename1 = "/opt/btlogger/BT-LOG.csv"

try:
    inputfile = open(input_filename1, "r")
    inputfile_data = inputfile.readlines()
    inputfile.close()
except:
    print "error opening inputfile!!!!"


all_macs = []
all_vendors = []
all_types = []
all_types2 = []
all_types3 = []
all_types4 = []
all_types5 = []
all_types6 = []

x = 0

for results in inputfile_data:
    try:
        results2 = results.split(";")
        newmac = results2[1]
        newvendor = results2[2]
        newtype = results2[3]
        newtype2 = results2[4]
        newtype3 = results2[5]
        newtype4 = results2[6]
        newtype5 = results2[7]
        newtype6 = results2[8]
    except:
        pass
        print "error setting new result types !!!!"
    try:
        all_macs.append(newmac)
        all_vendors.append(newvendor)
        all_types.append(newtype)
        all_types2.append(newtype2)
        all_types3.append(newtype3)
        all_types4.append(newtype4)
        all_types5.append(newtype5)
        all_types6.append(newtype6)
    except:
        pass
        print "error with counter lists!"


try:
    #Counter(all_macs)
    mac_counts = Counter(all_macs)
    mac_counts_str = str(mac_counts)
    vendor_counts = Counter(all_vendors)
    vendor_counts_str = str(vendor_counts)
    fmcounts = mac_counts.most_common()
    fvcounts = vendor_counts.most_common()
    type_counts = Counter(all_types)
    type_counts_str = str(type_counts)
    type2_counts = Counter(all_types2)
    type2_counts_str = str(type2_counts)
    type3_counts = Counter(all_types3)
    type3_counts_str = str(type3_counts)
    type4_counts = Counter(all_types4)
    type4_counts_str = str(type4_counts)
    type5_counts = Counter(all_types5)
    type5_counts_str = str(type5_counts)
    type6_counts = Counter(all_types6)
    type6_counts_str = str(type6_counts)
    typecounts = type_counts.most_common()
    typecounts2 = type2_counts.most_common()
    typecounts3 = type3_counts.most_common()
    typecounts4 = type4_counts.most_common()
    typecounts5 = type5_counts.most_common()
    typecounts6 = type6_counts.most_common()
except:
    pass
    print "error MAJOR on counters/strings !!!!"


with open ("/opt/btlogger/BT-totals.txt", "w") as outputfile:
    total_macs = str(len(set(all_macs)))
    total_btconns = str(len(all_macs))
    output0 = total_macs + "," + total_btconns
    outputfile.write(output0)

total_venconns = len(fvcounts)
total_venconns = str(total_venconns)

with open ("/opt/btlogger/BT-scores.txt", "w") as outputfile:
    outputfile.write("TOTAL UNIQUE MAC ADDRS:" + "\n")
    outputfile.write(total_macs + "\n\n")
    outputfile.write("TOTAL OBSERVED VENDORS:" + "\n")
    outputfile.write(total_venconns + "\n\n")
    outputfile.write("TOTAL BLUETOOTH CONNECTIONS:" + "\n")
    outputfile.write(total_btconns + "\n\n")

with open ("/opt/btlogger/BT-macaddr.txt", "w") as outputfile:
    outputfile.write("TOP OBSERVED MAC ADDRS:" + "\n")
    for x in mac_counts:
        outputfile.write(x + "\n")
        #print x + "\n"

with open ("/opt/btlogger/BT-vendors.txt", "w") as outputfile:
    outputfile.write("TOP OBSERVED VENDORS:" + "\n")
    allvendors = set(all_vendors)
    for y in allvendors:
        outputfile.write(y + "\n")
        #print y + "\n"

#print "\n"

print "=============================================="
print "TOP OBSERVED BLUETOOTH VENDORS"
print "=============================================="
for vendors in fvcounts:
        print vendors

print "\n"

print "=============================================="
print "TOP 20 OBSERVED MAC ADDRESSES WITH COUNTS"
print "=============================================="

while x < 20:
    try:
        print fmcounts[x]
    except:
        pass
    x = x + 1

print "\n"

print "TOTAL UNIQUE MAC ADDRS:"
print len(set(all_macs))

print "\n"

print "TOTAL UNIQUE VENDORS:"
print len(set(all_vendors))

print "\n"

print "TOTAL BLUETOOTH CONNECTIONS OBSERVED"
print len(all_macs)

print "\n\n"

print "======================================="
print "INTERESTING STRINGS FROM COLUMN 3" + "\n"
for stuff in typecounts:
    if len(stuff[0]) < 16:
        print stuff
    if len(stuff[0]) > 16:
        if (stuff[0][2] and stuff[0][5] != "-"):
            if (stuff[0][2] and stuff[0][5] != ":"):
                print stuff

print "\n"
print "======================================="
print "INTERESTING STRINGS FROM COLUMN 4" + "\n"
for stuff2 in typecounts2:
    if stuff2:
        if len(stuff2[0]) == 17:
            if (stuff2[0][2]) != "-":
                if (stuff2[0][5]) != ":":
                    if (stuff2[0][0]) != "-":
                        if (stuff2[0][0]):
                            print stuff2
        try:
            if len(stuff2[0]) != 17:
                if (stuff2[0][0]) != "-":
                    if (stuff2[0][0]):
                        if len(stuff2[0]) > 1:
                            print stuff2
        except:
            pass
            #print "ruh roh!" + stuff2 + "ruh roh!"

print "\n"
print "======================================="
print "INTERESTING STRINGS FROM COLUMN 5" + "\n"
for stuff3 in typecounts3:
    if stuff3:
        if stuff3[0]:
            if stuff3[0][0] != "-":
                if len (stuff3[0]) > 1:
                    print stuff3


print "\n"
print "======================================="
print "INTERESTING STRINGS FROM COLUMN 6" + "\n"
for stuff4 in typecounts4:
    if stuff4:
        if stuff4[0]:
            if stuff4[0][0] != "-":
                if len (stuff4[0]) > 1:
                    print stuff4



print "\n"
print "======================================="
print "INTERESTING STRINGS FROM COLUMN 7" + "\n"
for stuff5 in typecounts5:
    if stuff5:
        if stuff5[0]:
            if stuff5[0][0] != "-":
                if len (stuff5[0]) > 1:
                    print stuff5


print "\n"
print "======================================="
print "INTERESTING STRINGS FROM COLUMN 8" + "\n"
for stuff6 in typecounts6:
    if stuff6:
        if stuff6[0]:
            if stuff6[0][0] != "-":
                if len (stuff6[0]) > 1:
                    print stuff6

print "\n\n"

sys.exit()


