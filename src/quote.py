"""
Simple python script to run on bash start up.
This will print a welcome message and then a random quote from a text file

9-27-17
Jeffery Russell
"""

import random
import sys
import os.path

import glob

from utils import module
from utils import print_message_bubble
import configuration


"""Path to a text file containing quotes"""
INPUT_FILE = configuration.get_config()["quotes"]

"""Pulls a list of the ascii art file names"""
BASE_FILE = os.path.dirname(os.path.realpath(__file__))
ASCII_ART = glob.glob(BASE_FILE + "/asciiArt/*.txt")


def print_message(message, ascii_file = None):
    """
    Prints a dialog box with a message in it with an ascii
    animal below it
    :param message: a quote to print
    :param ascii_file: the file location of the ascii art speaking the message
    :return: NA
    """
    print_message_bubble.print_message(message)
    if ascii_file != None:
        filepath = '/'.join(INPUT_FILE.split('/')[:-1])
        filepath += "/asciiArt/" + ascii_file
        f = open(filepath, 'r')
        print(f.read())
        f.close()
    else:
        print(module.input_file_with_new_line(
            ASCII_ART[random.randint(0,(len(ASCII_ART) -1))]))


def print_usage():
    """
    Prints the usage message to the terminal
    :return: None
    """
    print("Usage:")
    print("\t-a quote \t: Adds a quote to the quotes list")
    print("\t-h \t\t: Prints usage message")


def add_quote():
    """
    Adds the quote in the command line arguments
    to the quotes text file
    :return: None
    """
    quote = ""

    for i in range(2, len(sys.argv)):
        quote = quote + sys.argv[i]
        quote = quote + " "

    print("added " + quote + "to " + INPUT_FILE)
    module.append_file(INPUT_FILE, quote)


def main():
    """
    This function calls the welcome function, then it calls the cowsay
    function with a random quote.
    :return: None
    """
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "-h" or sys.argv[1].lower() == "-help":
            print_usage()
        elif sys.argv[1].lower() == "-a":
            if len(sys.argv) > 2:
                add_quote()
            else:
                print("You forgot to enter a quote.")
        elif sys.argv[1][:2] == "--":
            quotes = module.input_file(INPUT_FILE)
            print_message(quotes[random.randint(0,(len(quotes) -1))], ascii_file=sys.argv[1][2:]+'.txt')
        else:
            print_usage()
    else:
        quotes = module.input_file(INPUT_FILE)

        if len(quotes) == 0:
            print("Quotes file : " + INPUT_FILE + " is empty.")
        else:
            print_message(quotes[random.randint(0,(len(quotes) -1))])


"""
Makes sure that other programs don't execute the main
"""
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
