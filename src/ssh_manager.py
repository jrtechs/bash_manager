"""
Jeffery Russell
9-26-17
"""

import subprocess
import collections

INPUT_FILE = "/home/jeff/scripts/servers.txt"
Computer = collections.namedtuple("Computer", ('host', 'menue_id'))

def main():


    cmp = []
    count = 1
    with open(INPUT_FILE) as file:
        for line in file:
            cmp.append(Computer(line, count))
            count += 1

    print("SSH manager V 0.1")
    for c in cmp:
        print(str(c.menue_id) + ")", c.host)
    print()
    i = input("Enter number of computer to connect to or enter to exit:")

    for c in cmp:
        if i != '' and int(i) == c.menue_id:
            subprocess.call(["ssh", c.host.strip(' \t\n\r')])

"""
Makes sure that other programs don't execute the main
"""
if __name__ == '__main__':
        main()