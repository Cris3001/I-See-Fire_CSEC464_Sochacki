#!/usr/bin/python
# Firewall Tool By: Cristofer Sochacki
import subprocess


def printRules():
    rules = subprocess.call(["sudo", "iptables", "-S"])
    print(rules)

def main():
    print('running')
    printRules()
    return

if __name__ == "__main__":
    main()
#input("Enter: ")