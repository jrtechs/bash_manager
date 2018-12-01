"""
Jeffery Russell
9/29/17
"""

import subprocess
import os.path


def input_file(file_name):
    """
    This file inputs the file defined by INPUT_FILE into a string line and returns it
    :return: a string array containing the lines of INPUT_FILE
    """
    f = []
    with open(file_name.strip('\n')) as file:
        for line in file:
            f.append(line.strip(' \t\n\r'))
    return f

def check_file_exists(fileloc):
    """
    Function which checks to see if a file exists
    :return: whether file exists
    """
    return os.path.exists(fileloc)


def append_file(file_name, append):
    """
    Appends text to bottom of a text file
    :param file_name: name of file
    :param append: message to append on file
    :return: None
    """
    file_name = os.path.expanduser(file_name)
    f = open(file_name, "a+")
    f.write(append + "\n")
    f.close()


def remove_line_from_file(file_name, remove):
    """
    removes a single line of text from a text file
    :param file_name:
    :param remove:
    :return:
    """
    lines = input_file(file_name)
    f = open(file_name, "w")
    for host in lines:
        if remove not in host:
            f.write(host + "\n")
    f.close()


def create_empty_file(file_name):
    """
    simple function to create a new file on system
    """
    file_name = file_name.replace('\n', '')
    subprocess.call(['touch', file_name])


TOP_BAR = "**************************************"


def print_magenta(prt): return"\033[95m {}\033[00m" .format(prt)


def print_green(prt): return "\033[92m {}\033[00m" .format(prt)


def print_red(prt): return "\033[91m {}\033[00m" .format(prt)


def print_menu_option(s):
    """
    Prints each host option
    :param s:
    :return:
    """
    space = " " * (len(TOP_BAR) - 4 - len(s))
    print(print_magenta("* ") + s + space + print_magenta("*"))  


def print_menu(name, lines):
    """
    Function which prints a nice menu for the user (box thing)

    ex:

    **************************************
    *          SSH Drive Manager         *
    * 1) Remove Remote Drive             *
    * 2) Add Drive to Mount              *
    * 3) View Drives                     *
    * 4) Exit                            *
    **************************************

    """
    if not len(name) % 2 == 0:
        name = name + " "
    spaces = len(TOP_BAR) - 4 - len(name)

    print(print_magenta(TOP_BAR))

    print(print_magenta("*") + 
        (int(spaces/2) * " ") + 
        print_green(name) + 
        (int(spaces/2) * " ") + 
        print_magenta("*"))

    for s in lines:
        print_menu_option(s)
    print(print_magenta(TOP_BAR))