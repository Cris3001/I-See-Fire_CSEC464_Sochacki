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
    status = open("temp2.txt", "r")
    status_out = status.readline()
    treeview.insert('hi', 'end', values=(status_out, 'hi'))
    status.close()
    return status_out


def main():

    return


if __name__ == "__main__":
    main()
