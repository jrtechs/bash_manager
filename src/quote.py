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

"""Path to a text file containing quotes"""
INPUT_FILE = "/home/jeff/scripts/quotes.txt"


def print_cowsay_message(message):
    """
    Runs the cowsay command and passes it message to print
    :param message: The message to print
    :return: None
    """
    subprocess.call(["cowsay", message])


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
    #print_cowsay_message(quotes[random.randint(0,(len(quotes) -1))])
    print_roosay_message(quotes[random.randint(0,(len(quotes) -1))])


"""
Makes sure that other programs don't execute the main
"""
if __name__ == '__main__':
        main()