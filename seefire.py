#!/usr/bin/python
# Firewall Tool By: Cristofer Sochacki
from subprocess import *
import gui



def getRules():
    rules = subprocess.Popen(["sudo", "iptables", "-S", ">"], stdout=PIPE)
    out = rules.communicate()
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