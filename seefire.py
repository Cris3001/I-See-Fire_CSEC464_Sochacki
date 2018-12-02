#!/usr/bin/python
# Firewall Tool By: Cristofer Sochacki
import subprocess
import os
from subprocess import *
import gui



def getRules():
#    subprocess.run(["sudo", "iptables", "-S", ">", "temp.txt"])
    os.system("sudo iptables -S > temp.txt")
    rules = open("temp.txt", "r")
    rulesOut = rules.read()
    rules.close()
#    out = rules.stdout
#    rules = "the rules\n"
    return rulesOut


def main():
    print('running')
    is_sudo = os.getenv("SUDO_USER")
    if(is_sudo == None):
        print("Program must be run with sudo")
        exit()
#    printRules()
    app = gui.Window(gui.root)
    gui.root.mainloop()
    return

if __name__ == "__main__":
    main()
#input("Enter: ")