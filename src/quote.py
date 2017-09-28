"""
Simple python script to run on bash start up.
This will print a welcome message and then a random quote from a text file

9-27-17
Jeffery Russell
"""

import subprocess
import random

INPUT_FILE = "/home/jeff/scripts/quotes.txt"
WELCOME_MESSAGE = "***************Jeff-Laptop*************"


def print_cowsay_message(message):
    """
    Runs the cowsay command and passes it message to print
    :param message: The message to print
    :return: None
    """
    subprocess.call(["cowsay", message])


def print_welcome_message():
    """
    Prints defined greeting message to terminal
    :return: None
    """
    print(WELCOME_MESSAGE)


def input_file():
    """
    This file inputs the file defined by INPUT_FILE into a string line and returns it
    :return: a string array containing the lines of INPUT_FILE
    """
    quotes = []
    with open(INPUT_FILE) as file:
        for line in file:
            quotes.append(line.strip(' \t\n\r'))
    return quotes

def main():
    """
    This function calls the welcome function, then it calls the cowsay function with a random quote.
    :return: None
    """

    quotes = input_file()

    print_cowsay_message(quotes[random.randint(0,(len(quotes) -1))])

    print_welcome_message()


"""
Makes sure that other programs don't execute the main
"""
if __name__ == '__main__':
        main()