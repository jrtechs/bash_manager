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
    print(magenta_print(WELCOME_MESSAGE))


def print_menu_option(s):
    """

    :param s:
    :return:
    """
    space = " " * (len(WELCOME_MESSAGE) - 3 - len(s))
    print(magenta_print("*") + s + space + magenta_print("*"))


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

    print(magenta_print("*") + "         SSH manager V 0.2         " + magenta_print("*"))
    for c in cmp:
        print_menu_option(str(c.menue_id) + ") " + c.host)

    print_menu_option("A) Exit")
    print_menu_option("B) Manager tools")

    print(magenta_print("*" * len(WELCOME_MESSAGE)))
    i = input("Enter number of computer to connect to or enter to exit:")

    if i == '' or i == 'A' or i == 'a':
        exit_program()
    elif i == 'b' or i == 'B':
        sub_menu()
    else:
        for c in cmp:
            if int(i) == c.menue_id:
                subprocess.call(["ssh", c.host])


def print_sub_menu():
    """
    prints out a sub help menu for other options
    :return: None
    """
    print(magenta_print("**************************************"))
    print(magenta_print("*") + "     SSH manager V 0.2 Options     " + magenta_print("*"))
    print_menu_option("1) Add Host")
    print_menu_option("2) Copy SSH key to server")
    print_menu_option("3) Remove host name")
    print_menu_option("4) Return to ssh manager")
    print_menu_option("5) Exit")
    print(magenta_print("*" * len(WELCOME_MESSAGE)))


def magenta_print(prt): return"\033[95m {}\033[00m" .format(prt)


def sub_menu():
    """
    calls printSubMenu and then gets input from user to make appropriate function calls
    :return: None
    """
    print_sub_menu()
    i = input("Enter selection:")

    if i != '' and int(i) in {1, 2, 3, 4, 5}:
        options = {1: add_host,
                   2: copy_ssh_key,
                   3: remove_host,
                   4: main,
                   5: exit_program,
                   }
        options[int(i)]()
    else:
        print("Invalid selection!")

    sub_menu()


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
    host = input("enter host name or -1 to exit:")
    if host != '-1':
        module.append_file(INPUT_FILE, host)


def copy_ssh_key():
    """
    calls systems ssh-copy-id with host name
    :return: None
    """
    host = input("enter user@host or -1 to exit:")
    if host != '-1':
        subprocess.call(["ssh-copy-id " + host])


def remove_host():
    """
    Removes a host name from servers.txt
    :return: None
    """
    host = input("enter host to remove or -1 to exit:")
    if host != '-1':
        module.remove_line_from_file(INPUT_FILE, host)

"""
Makes sure that other programs don't execute the main
"""
if __name__ == '__main__':
        main()
