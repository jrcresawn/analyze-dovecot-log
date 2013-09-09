#!/usr/bin/env python

import argparse, re, socket

parser = argparse.ArgumentParser()
parser.add_argument("user")
parser.add_argument("log")
args = parser.parse_args()

r = re.compile('^.*rip=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*$')

rip = {}
unsecure = {}

with open(args.log) as input:
    for line in input:
        m = r.match(line)
        if args.user in line:
            if m:
                if m.group(1) in rip:
                    rip[m.group(1)] = rip[m.group(1)] + 1
                else:
                    rip[m.group(1)] = 1

                if not "TLS" in line and not "secured" in line:
                    unsecure[m.group(1)] = 1
                else:
                    unsecure[m.group(1)] = 0

print "IP ADDRESS,FQDN,SECURITY,# CONNECTIONS"
for k in rip.keys():
    try:
        h = socket.gethostbyaddr(k)[0]
    except:
        h = ""

    if unsecure[k]:
        print k + "," + h + ",unsecure," + str(rip[k])
    else:
        print k + "," + h + ",secure," + str(rip[k])
