#!/usr/bin/python
# Firewall Tool By: Cristofer Sochacki
import subprocess
from subprocess import *
import gui



def getRules():
    rules = subprocess.run(["sudo", "iptables", "-S", ">"], stdout=PIPE)
    out = rules.stdout
#    rules = "the rules\n"
    return out


def main():
    print('running')
#    printRules()
    app = gui.Window(gui.root)
    gui.root.mainloop()
    return

if __name__ == "__main__":
    main()
#input("Enter: ")