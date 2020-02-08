"""
Jeffery Russell
9-26-17
"""

import subprocess
import collections

from utils import module
import configuration
import mount_ssh_drive

INPUT_FILE = configuration.get_config()["servers"]

Computer = collections.namedtuple("Computer", ('host', 'menu_id'))

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
        menu.append(str(c.menu_id) + ") " + c.host)
    menu.append("A) Exit")
    menu.append("B) Manager tools")
    menu.append("C) Socks Tunnel")
    menu.append("D) SSH Drive Manager")

    module.print_menu("SSH manager V 1.0 ", menu)

    i = input("Enter Option:")

    if i == '' or i == 'A' or i == 'a':
        exit_program()
    elif i == 'b' or i == 'B':
        sub_menu()
    elif "c" == str.lower(i):
        socks_ssh_tunnel()
    elif "d" == str.lower(i):
        mount_ssh_drive.main()
    else:
        for c in cmp:
            if int(i) == c.menu_id:
                subprocess.call(["ssh", c.host])
                exit_program()


def socks_ssh_tunnel():
    """
    prints user a menu to select a host to start a socks proxy with
    :return: None
    """
    file = module.input_file(INPUT_FILE)
    cmp = []
    count = 1
    for line in file:
        cmp.append(Computer(line, count))
        count += 1

    menu = []
    for c in cmp:
        menu.append(str(c.menu_id) + ") " + c.host)

    menu.append("A) Exit")
    menu.append("B) Main")
    module.print_menu("Socks Tunnel", menu)


    i = input("Enter option:")
    if i == '' or 'a' == str.lower(i):
        exit_program()
    elif 'b' == str.lower(i):
        main()
    else:
        for c in cmp:
            if int(i) == c.menu_id:
                print_red("Starting socks proxy on " + c.host + ":8123")
                subprocess.call(["ssh", "-D", "8123", "-C", "-q", "-N", c.host])
                exit_program()


def print_sub_menu():
    """
    prints out a sub help menu for other options
    :return: None
    """
    module.print_menu("Options", ["1) Add Host",
                                "2) Copy SSH key to server",
                                "3) Remove host name",
                                "4) Return to ssh manager",
                                "5) Manage Configuration and Bash",
                                "6) Exit"])


def print_red(prt): return "\033[91m {}\033[00m" .format(prt)


def sub_menu():
    """
    calls printSubMenu and then gets input from user to 
    make appropriate function calls
    :return: None
    """
    print_sub_menu()
    i = input("Enter selection:")

    if i != '' and int(i) in {1, 2, 3, 4, 5, 6}:
        options = {1: add_host,
                   2: copy_ssh_key,
                   3: remove_host,
                   4: main,
                   5: configuration.main,
                   6: exit_program
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
    host = input("Enter 'user@host' or -1 to exit:")
    if host != '-1':
        module.append_file(INPUT_FILE, host)


def copy_ssh_key():
    """
    calls systems ssh-copy-id with host name
    :return: None
    """
    file = module.input_file(INPUT_FILE)
    cmp = []
    count = 1
    for line in file:
        cmp.append(Computer(line, count))
        count += 1

    menu = []
    for c in cmp:
        menu.append(str(c.menu_id) + ") " + c.host)
    menu.append("A) Exit")
    module.print_menu("Copy SSH Key", menu)

    host_id = input("Enter number of host to copy ssh key to:")
    if not (host_id == '-1' or host_id.lower() == 'a'):
        for c in cmp:
            if c.menu_id == int(host_id):
                subprocess.call(["ssh-copy-id", c.host])


def remove_host():
    """
    Removes a host name from servers.txt
    :return: None
    """
    file = module.input_file(INPUT_FILE)
    cmp = []
    count = 1
    print(print_red("*" * len(WELCOME_MESSAGE)))
    for line in file:
        cmp.append(Computer(line, count))
        count += 1
    for c in cmp:
        space = " " * (len(WELCOME_MESSAGE) - 3 - 
                len(str(c.menu_id) + ") " + c.host))
        print(print_red("*") + str(c.menu_id) + ") " + 
            c.host + space + print_red("*"))

    print(print_red("*" * len(WELCOME_MESSAGE)))

    host = input("Enter number of host -1 to exit:")
    if host != '-1':
        for c in cmp:
            if c.menu_id == int(host):
                module.remove_line_from_file(INPUT_FILE, c.host)


"""
Makes sure that other programs don't execute the main
"""
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit_program()
