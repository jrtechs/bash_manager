"""
Makes sure that other programs don't execute the main
"""

import sys

def main():
    """

    :return:
    """
    message  = ""
    for i in range(1, len(sys.argv)):
        message += sys.argv[i]

    roo_say(message)


def roo_say(message):
    print_message(message)
    print_roo()


def print_message(message):
    print_list, max_len = convert_to_list(message)

    if len(print_list) > 0:
        """Print top"""
        print(" " + "-" * (max_len + 2))

        "print middle"
        if len(print_list) == 1:
            print("< " + print_list[0] + " >")
        else:
            for i in range(0)

    else:
        print("Please pass in a message parameter")




def convert_to_list(message):
    temp_build = ""
    temp_return = []
    max_len = 0
    for word in message.split(" "):
        if len(temp_build) + len(word) <= 35:
            temp_build += word
        else:
            temp_return.append(temp_build)
            if max_len < len(temp_build):
                max_len = len(temp_build)
            temp_build = word
    if len(temp_build) > 0:
        temp_return.append(temp_return)
    return temp_return, max_len


def print_roo():
    print("")
    print("           \    /)/)")
    print("            \  (ø.ø)")
    print("                \ (    />")
    print("              __/ _\  //")
    print("             '~( '~ )//")
    print("               _\  '}/")
    print("              \"--~(/")


if __name__ == '__main__':
        main()