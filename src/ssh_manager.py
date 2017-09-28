"""
Jeffery Russell
9-26-17
"""

import subprocess
import collections

import quote

INPUT_FILE = "/home/jeff/scripts/servers.txt"
Computer = collections.namedtuple("Computer", ('host', 'menue_id'))
WELCOME_MESSAGE = "***************Jeff-Laptop***************"

def print_menu_option(s):
    """

    :param s:
    :return:
    """
    space = " " * len(quote) - 4 - len(s)
    print("* " + s + space + "*")

def main():
    """
    This function inputs all the available hosts from a text file and prompts the user to connect to them
    :return:
    """

    cmp = []
    count = 1
    with open(INPUT_FILE) as file:
        for line in file:
            cmp.append(Computer(line, count))
            count += 1

    print("*          SSH manager V 0.1           *")
    for c in cmp:
        print_menu_option(str(c.menue_id) + ") " + c.host)

    print("*" * len(WELCOME_MESSAGE))
    i = input("Enter number of computer to connect to or enter to exit:")

    for c in cmp:
        if i != '' and int(i) == c.menue_id:
            subprocess.call(["ssh", c.host.strip(' \t\n\r')])

"""
Makes sure that other programs don't execute the main
"""
if __name__ == '__main__':
        main()