import roosay
import sys
import pyfiglet
def main():
    """
    checks for command line arguments
    :return: None
    """
    message  = ""
    for i in range(1, len(sys.argv)):
        if len(message) > 0:
            message += " "
        message += sys.argv[i]
    
    if len(message) == 0:
        for line in sys.stdin:
            message+= line

    message = " ".join(message.split())
    batsay(message)

def batsay(message):
    """
    prints message through roosay print
    message function the prints bat.
    :param message: the message to print
    :return: None
    """
    roosay.print_message(message)
    print_bat()

def print_bat():
    """
    prints bat ascii
    :return: None
    """
    print("             \             ")
    print("     /\       \         /\ ")
    print("    / \\'._   (\_/)   _.'/ \ ")
    print("    |.''._'--(o.o)--'_.''.|")
    print('     \_ / `;=/ " \=;` \ _/ ')
    print("       `\__| \___/ |__/`   ")
    print("            \(_|_)/        ")
    print('             " ` "         ')

if __name__ == '__main__':
    main()
def thanks_and_exit():
    print(pyfiglet.figlet_format('Thank you',font='slant'))
    sys.exit()
