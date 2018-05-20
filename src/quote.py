"""
Simple python script to run on bash start up.
This will print a welcome message and then a random quote from a text file

9-27-17
Jeffery Russell
"""

import subprocess
import random

import module
import roosay
import configuration


"""Path to a text file containing quotes"""
INPUT_FILE = configuration.get_config()["quotes"]


def print_roosay_message(message):
    """
    Calls the roosay command that prints an ascii roo with a message above it
    :param message: a quote to print
    :return:
    """
    roosay.roo_say(message)


def main():
    """
    This function calls the welcome function, then it calls the cowsay function with a random quote.
    :return: None
    """
    quotes = module.input_file(INPUT_FILE)

    if len(quotes) == 0:
        print("Quotes file : " + INPUT_FILE + " is empty.")
    else:
        print_roosay_message(quotes[random.randint(0,(len(quotes) -1))])


"""
Makes sure that other programs don't execute the main
"""
if __name__ == '__main__':
        main()