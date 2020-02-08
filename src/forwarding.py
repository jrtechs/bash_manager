"""
Author: Jason Cheung
Date: 2/8/2020

Description: This is a manager for easily performing SHH port forwards
"""

import subprocess
import collections

from utils import module
import configuration

# INPUT_FILE = configuration.get_config()["portforwards"]
INPUT_FILE = "./portforwards.txt"
Computer = collections.namedtuple("Computer", ('user', 'user_num'))
WELCOME_MESSAGE = "**************************************"


def main():
    """
    This function inputs all the available hosts from a text file and
    prompts the user to connect to them
    :return:
    """
    file = module.input_file(INPUT_FILE)

    cmp = []
    count = 1

    for line in file:
        cmp.append(Computer(line, count))
        count += 1
    menu = []

    for c in cmp:
        menu.append(str(c.user_num) + ") " + "".join(c.user))
    menu.append("A) Exit")
    menu.append("B) Manager tools")

    module.print_menu("SSH forwarding manager V 1.0", menu)

    i = input("Enter Option:")

    if i == '' or i == 'A' or i == 'a':
        exit_program()
    elif i == 'B' or i == 'b':
        sub_menu()
    else:
        for c in cmp:
            if int(i) == c.user_num:
                subprocess.call(
                    ["ssh", "-L", c.user.split(":")[2] + ":localhost:"
                     + c.user.split(":")[2], c.user.split(":")[1]])
                exit_program()


def print_sub_menu():
    """
    prints out a sub help menu for other options
    :return: None
    """
    module.print_menu("Options", ["1) Add Host",
                                  "2) Remove host name",
                                  "3) Return to ssh forwarding",
                                  "4) Manage Configuration and Bash",
                                  "5) Exit"])


def sub_menu():
    """
    calls printSubMenu and then gets input from user to
    make appropriate function calls
    :return: None
    """
    print_sub_menu()
    i = input("Enter selection:")

    if i != '' and int(i) in {1, 2, 3, 4, 5}:
        options = {1: add_host,
                   2: remove_host,
                   3: main,
                   4: configuration.main,
                   5: exit_program
                   }
        options[int(i)]()
    else:
        print("Invalid selection!")

    sub_menu()


def print_red(prt): return "\033[91m {}\033[00m".format(prt)


def exit_program():
    """
    Exits the program and clears the screen
    :return: None
    """
    subprocess.call(["clear"])
    exit()


def add_host():
    """
    appends an inputted host name to servers.txt
    :return: None
    """
    host = input("Enter 'user@host' or -1 to exit:")
    if host != '-1':
        name = input("Name: ")
        port = input("Port: ")
        module.append_file(INPUT_FILE, name + ":" + host + ":" + port)


def remove_host():
    """
    Removes a host name from servers.txt
    :return: None
    """
    padding_star = "*" * 5
    max_len = 0
    file = module.input_file(INPUT_FILE)
    for line in file:
        temp = len(line)
        if max_len < temp:
            max_len = temp
    TOP_BAR = padding_star + "*" * max_len + padding_star
    cmp = []
    count = 1
    print(print_red("*" * len(TOP_BAR) + "*"))
    for line in file:
        cmp.append(Computer(line, count))
        count += 1
    for c in cmp:
        space = " " * (len(TOP_BAR) - 3 -
                       len(str(c.user_num) + ") " + c.user))
        print(print_red("*") + " " + str(c.user_num) + ") " +
              c.user + space + print_red("*"))

    print(print_red("*" * len(TOP_BAR) + '*'))

    host = input("Enter number of host -1 to exit:")
    if host != '-1':
        for c in cmp:
            if c.user_num == int(host):
                module.remove_line_from_file(INPUT_FILE, c.user)


"""
Makes sure that other programs don't execute the main
"""
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit_program()
