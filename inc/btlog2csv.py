#!/usr/bin/python
import subprocess
import time
import datetime
import re

inputfile2 = open("/opt/btlogger/inc/tags.txt", "r")
searchlines2 = inputfile2.readlines()
inputfile2.close()

mac_cache = {}

total_tags = len(searchlines2)

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

ansi_escape = re.compile(r'\x1b[^m]*m')


if __name__ == '__main__':
    logfile = open("/opt/btlogger/BT-LOG.txt","r")
    loglines = follow(logfile)
    for line in loglines:
        #print line,
        line = line.strip("\r")
        line = ansi_escape.sub('',line)
        #if line[0] != '\x1b'  or '\r' or '':
        try:
            newline = line.split()
            if line[8] != None or len(newline) != 1:
                #print len(newline)
                #print "\n"
                #print newline
                macaddr1 = newline[2]
                #print macaddr1 + "!!!!!!!!!!!"
                if macaddr1 == "Device":
                    macaddr1 = newline[3]
                if macaddr1 == "[CHG]":
                    macaddr1 = newline[4]
                if macaddr1 == "CHG]":
                    macaddr1 = newline[4]
                if macaddr1[2] != ":":
                    macaddr1 = ""
                if macaddr1 == "Device":
                    macaddr1 = newline[3]
                    #if macaddr1 == "[CHG]":
                    #    macaddr1 = ""
                try:
                    result2 = newline[1]
                    if result2 != "Device":
                        result2 = "Device!"
                    result2 = newline[1]
                except:
                    pass
                    result2 = ""
                try:
                    result3 = newline[3]
                except:
                    pass
                    result3 = ""
                try:
                    result4 = newline[4]
                except:
                    pass
                    result4 = ""
                try:
                    result5 = newline[5].replace(" ","-")
                except:
                    pass
                    result5 = ""
                try:
                    result6 = newline[6].replace(" ","-")
                except:
                    pass
                    result6 = ""
                try:
                    result7 = newline[7].replace(" ","-")
                except:
                    pass
                    result7 = ""
                try:
                    result8 = newline[8].replace(" ","-")
                except:
                    pass
                    result8 = ""
                try:
                    result9 = newline[9].replace(" ","-")
                except:
                    pass
                    result9 = ""
                try:
                    result10 = newline[10].replace(" ","-")
                except:
                    pass
                    result10 = ""
                #print macaddr1
                #print label,
                #print signal
                macaddr2 = macaddr1[0:8]
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
                        mac_cache[macaddr] = vendorname
                #print vendorname
                ts = time.time()
                st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                x = 0
                while x < total_tags:
                    for tags in searchlines2:
                        taggedmac = searchlines2[x].split(";")[0]
                        taggedmac = taggedmac.strip("\n")
                        goodtag = searchlines2[x].split(";")[1]
                        goodtag = goodtag.strip("\n")
                        x = x + 1
                        #print taggedmac
                        if macaddr1 == taggedmac:
                            macaddr1 = goodtag + " " + taggedmac
                            #print macaddr1
                output = st + ";" + macaddr1 + ";" + vendorname + ";" + result3 + ";" + result4 + ";" + result5 + ";" + result6 + ";" + result7 + ";" + result8 + ";" + result9 + ";" + result10 + "\n"
                try:
                    with open ("/opt/btlogger/BT-LOG.csv", "a") as outputfile:
                        #print macaddr1 + "!!!!!!!!!!!!!!!!!!"
                        if macaddr1 == "on" or macaddr1 == "started" or macaddr1 == "Controller" or macaddr1 == "Device":
                            macaddr = ""
                        if len(macaddr1) > 1 or newline[1][2] == ":":
                        #if len(macaddr1) > 1 or newline[1] != "on" or newline[1] != "()" or newline[1] != "connect" or newline[1] != "started":
                            outputfile.write(output)
                except:
                    pass
                    #print "error writing OUTPUT-BLUETOOTH.csv file!!!"
                st = ""
                macaddr = ""
                macaddr1 = ""
                vendorname = ""
                result2 = ""
                result3 = ""
                result4 = ""
                result5 = ""
                result6 = ""
                result7 = ""
                result8 = ""
                result9 = ""
                result10 = ""
                macaddr = ""
                key = ""
                newline = ""
        except:
            pass
            #print " ruh roh! "


