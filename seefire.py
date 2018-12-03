#!/usr/bin/python
# Firewall Tool By: Cristofer Sochacki
#import subprocess
import os
import ttk
from subprocess import *
import gui



def getRules():
    os.system("sudo iptables -S > temp.txt")
    rules = open("temp.txt", "r")
    rulesOut = rules.read()
    rules.close()
    return rulesOut


def getStatus(treeview):
    os.system("sudo cat /var/log/messages | grep \"iptables\" > temp2.txt")
    status = "temp2.txt"
    with open(status) as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            cleanline = line.strip()
            if ("Starting" in cleanline) or ("Stopping" in cleanline) or ("Started" in cleanline) or\
                    ("Stopped" in cleanline):
                splitline = cleanline.split(' ')
                date = splitline[0] + ' ' + splitline[2] + ' ' + splitline[3]
                status_string = splitline[6]
                treeview.insert('', 'end', text=date, value=status_string)
    fp.close()
    os.system("rm temp2.txt")
    return


def main():

    return


if __name__ == "__main__":
    main()
