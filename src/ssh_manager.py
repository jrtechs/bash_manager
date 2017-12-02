"""
Jeffery Russell
9-26-17
"""

import subprocess
import collections

import module

INPUT_FILE = "/home/jeff/scripts/servers.txt"
Computer = collections.namedtuple("Computer", ('host', 'menue_id'))
WELCOME_MESSAGE = "*************Jeff-Tower***************"


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

    print("*         SSH manager V 0.2          *")
    for c in cmp:
        print_menu_option(str(c.menue_id) + ") " + c.host)

    print_menu_option("A/' ') Exit")
    print_menu_option("B/' ') Manager tools")

    print("*" * len(WELCOME_MESSAGE))
    i = input("Enter number of computer to connect to or enter to exit:")

    if i == '' or i == 'A' or i == 'a':
        subprocess.call(["clear"])
    elif i == 'b' or i == 'B':
        subMenu()
    else:
        for c in cmp:
            if int(i) == c.menue_id:
                subprocess.call(["ssh", c.host])


def printSubMenu():
    """
    prints out a sub help menu for other options
    :return: None
    """
    print("**************************************")
    print("*     SSH manager V 0.2 Options      *")
    print_menu_option("1) Add Host")
    print_menu_option("2) Copy SSH key to server")
    print_menu_option("3) Remove host name")
    print_menu_option("4) Return to ssh manager")
    print_menu_option("5) Exit")
    print("*" * len(WELCOME_MESSAGE))


def subMenu():
    """
    calls printSubMenu and then gets input from user to make appropriate function calls
    :return: None
    """
    printSubMenu()
    input = input("Enter selection:")


def addHost():
    """
    appends an inputted host name to servers.txt
    :return: None
    """
    pass


def copySSHKey():
    """
    calls systems ssh-copy-id with host name
    :return: None
    """
    pass


def removeHost():
    """
    Removes a host name from servers.txt
    :return: None
    """
    pass


"""
Makes sure that other programs don't execute the main
"""
if __name__ == '__main__':
        main()
