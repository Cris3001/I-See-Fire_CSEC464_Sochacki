#!/usr/bin/python
# Firewall Tool By: Cristofer Sochacki
import subprocess
import gui



def getRules():
    rules = subprocess.call(["sudo", "iptables", "-S"])
#    rules = "the rules\n"
    return rules


def main():
    print('running')
#    printRules()
    app = gui.Window(gui.root)
    gui.root.mainloop()
    return

if __name__ == "__main__":
    main()
#input("Enter: ")