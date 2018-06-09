"""
Simple python script to run on bash start up.
This will print a welcome message and then a random quote from a text file

9-27-17
Jeffery Russell
"""

import random
import sys

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
        else:
            print_usage()
    else:
        quotes = module.input_file(INPUT_FILE)

        if len(quotes) == 0:
            print("Quotes file : " + INPUT_FILE + " is empty.")
        else:
            print_roosay_message(quotes[random.randint(0,(len(quotes) -1))])


"""
Makes sure that other programs don't execute the main
"""
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()