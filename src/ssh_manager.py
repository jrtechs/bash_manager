"""
Jeffery Russell
9-26-17
"""

import subprocess
import collections

import module
import configuration

INPUT_FILE = configuration.get_config()["servers"]

Computer = collections.namedtuple("Computer", ('host', 'menu_id'))

WELCOME_MESSAGE = "**************************************"


def print_welcome_message():
    """
    Prints defined greeting message to terminal
    :return: None
    """
    print(print_magenta(WELCOME_MESSAGE))


def print_menu_option(s):
    """
    Prints each host option
    :param s:
    :return:
    """
    space = " " * (len(WELCOME_MESSAGE) - 4 - len(s))
    print(print_magenta("* ") + s + space + print_magenta("*"))


def main():
    """
    This function inputs all the available hosts from a text file and 
    prompts the user to connect to them
    :return:
    """
    print_welcome_message()
    file = module.input_file(INPUT_FILE)

    cmp = []
    count = 1

    for line in file:
        cmp.append(Computer(line, count))
        count += 1

    print(print_magenta("*") + "         " + 
        print_green("SSH manager V 0.2") + "        " + print_magenta("*"))
    for c in cmp:
        print_menu_option(str(c.menu_id) + ") " + c.host)

    print_menu_option("A) Exit")
    print_menu_option("B) Manager tools")
    print_menu_option("C) Socks Tunnel")

    print(print_magenta("*" * len(WELCOME_MESSAGE)))
    i = input("Enter Option:")

    if i == '' or i == 'A' or i == 'a':
        exit_program()
    elif i == 'b' or i == 'B':
        sub_menu()
    elif "c" == str.lower(i):
        socks_ssh_tunnel()
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
    print_welcome_message()
    file = module.input_file(INPUT_FILE)
    cmp = []
    count = 1
    for line in file:
        cmp.append(Computer(line, count))
        count += 1

    print(print_magenta("*") + "         " + 
            print_green("Socks Tunnel") + "             " + print_magenta("*"))
    for c in cmp:
        print_menu_option(str(c.menu_id) + ") " + c.host)
    print_menu_option("A) Exit")
    print_menu_option("B) Main")
    print(print_magenta("*" * len(WELCOME_MESSAGE)))
    i = input("Enter option:")
    if i == '' or 'c' == str.lower(i):
        exit_program()
    elif 'c' == str.lower(i):
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
    print(print_magenta("**************************************"))
    print(print_magenta("*") + print_green("Options") + 
        "                           " + print_magenta("*"))
    print_menu_option("1) Add Host")
    print_menu_option("2) Copy SSH key to server")
    print_menu_option("3) Remove host name")
    print_menu_option("4) Return to ssh manager")
    print_menu_option("5) Exit")
    print(print_magenta("*" * len(WELCOME_MESSAGE)))


def print_magenta(prt): return"\033[95m {}\033[00m" .format(prt)


def print_green(prt): return "\033[92m {}\033[00m" .format(prt)


def print_red(prt): return "\033[91m {}\033[00m" .format(prt)


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
    host = input("Enter 'user@host' or -1 to exit:")
    if host != '-1':
        module.append_file(INPUT_FILE, host)


def copy_ssh_key():
    """
    calls systems ssh-copy-id with host name
    :return: None
    """

    print_welcome_message()
    file = module.input_file(INPUT_FILE)
    cmp = []
    count = 1
    for line in file:
        cmp.append(Computer(line, count))
        count += 1

    print(print_magenta("*") + "         " + 
        print_green("Copy SSH Key") + "             " + print_magenta("*"))
    for c in cmp:
        print_menu_option(str(c.menu_id) + ") " + c.host)

    print_welcome_message()
    host_id = input("Enter number of host to copy ssh key to:")
    if host_id != '-1':
        for c in cmp:
            if c.menu_id == int(host_id):
                subprocess.call(["ssh-copy-id", c.host])
    print("Host not found in list!")


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
        exit_program();
