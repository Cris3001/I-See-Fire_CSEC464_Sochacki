#!/usr/bin/python
# Firewall Tool By: Cristofer Sochacki
import subprocess
import os
from subprocess import *
import gui



def getRules():
    os.system("sudo iptables -S > temp.txt")
    rules = open("temp.txt", "r")
    rulesOut = rules.read()
    rules.close()
    return rulesOut


def main():

    return


if __name__ == "__main__":
    main()
