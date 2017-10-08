"""
Jeffery Russell
9-26-17
"""

import subprocess
import collections

import module

INPUT_FILE = "/home/jeff/scripts/servers.txt"
Computer = collections.namedtuple("Computer", ('host', 'menue_id'))
WELCOME_MESSAGE = "*************Jeff-Laptop***************"


def print_welcome_message():
    """
    Prints defined greeting message to terminal
    :return: None
    """
    print(WELCOME_MESSAGE)


def print_menu_option(s):
    """

    :param s:
    :return:
    """
    space = " " * (len(WELCOME_MESSAGE) - 3 - len(s))
    print("* " + s + space + "*")


def main():
    """
    This function inputs all the available hosts from a text file and prompts the user to connect to them
    :return:
    """
    print_welcome_message()
    file = module.input_file(INPUT_FILE)

    cmp = []
    count = 1

    for line in file:
        cmp.append(Computer(line, count))
        count += 1

    print("*         SSH manager V 0.1           *")
    for c in cmp:
        print_menu_option(str(c.menue_id) + ") " + c.host)

    print("*" * len(WELCOME_MESSAGE))
    i = input("Enter number of computer to connect to or enter to exit:")

    if i == '':
        subprocess.call(["clear"])
    else:
        for c in cmp:
            if int(i) == c.menue_id:
                subprocess.call(["ssh", c.host])


"""
Makes sure that other programs don't execute the main
"""
if __name__ == '__main__':
        main()