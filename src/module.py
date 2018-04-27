"""
Jeffery Russell
9/29/17
"""

import subprocess


def input_file(file_name):
    """
    This file inputs the file defined by INPUT_FILE into a string line and returns it
    :return: a string array containing the lines of INPUT_FILE
    """
    f = []
    with open(file_name) as file:
        for line in file:
            f.append(line.strip(' \t\n\r'))
    return f


def append_file(file_name, append):
    """
    Appends text to bottom of a text file
    :param file_name: name of file
    :param append: message to append on file
    :return: None
    """
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
    simple function to mimic touch command
    """
    subprocess.call(['touch', file_name])