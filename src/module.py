"""
Jeffery Russell
9/29/17
"""


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