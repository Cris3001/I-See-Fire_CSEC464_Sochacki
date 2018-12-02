#!/usr/bin/python
# Firewall Tool By: Cristofer Sochacki
import subprocess
from subprocess import *
import gui



def getRules():
    run(["sudo", "iptables", "-S", ">", "temp.txt"])
    rules = open("./temp.txt", "r")
    rulesOut = rules.read()
    rules.close()
#    out = rules.stdout
#    rules = "the rules\n"
    return rulesOut


def main():
    print('running')
#    printRules()
    app = gui.Window(gui.root)
    gui.root.mainloop()
    return

if __name__ == "__main__":
    main()
#input("Enter: ")