"""
Jake Zaia
2018-10-12

Manages SSH config files, and supports a more user-friendly terminal based way of creating them
"""

import os

#This is the location of where the SSH
SSH_CONFIG_FILE_LOC = os.path.expanduser('~/.ssh/config')


def config_exists():
    """
    Checks if an SSH config file exists at the desired path
    """
    return os.path.isfile(SSH_CONFIG_FILE_LOC)

def get_config():
    """
    Returns the contents of the SSH config file as a string
    """
    if not config_exists():
        return ''
    f = open(SSH_CONFIG_FILE_LOC, 'r')
    ret = f.read()
    f.close()
    return ret

#TODO: check for duplicates, ensure no duplicate entries
def create_config():
    """
    Creates an SSH config file with information taken from a user
    """

    print("Please input the relevent information for generating your config file.")
    host = input("Nickname for Host: ")
    hostname = input("Hostname: ")
    user = input("Username: ")

    #Port is optional
    port = input("Would you like to specify a port?(y/N)")
    if (port == 'y' or port == 'Y' or port.lower() =='yes'):
        port = input("Port number: ")
    else:
        port = None

    #SSH public key location is optional
    identityfile = input("Would you like to specify an ssh public key location?(y/N)")
    if (identityfile == 'y' or identityfile == 'Y' or identityfile.lower() =='yes'):
        identityfile = input("SSH Public key file location: ")

    #Write info to config file
    if config_exists():
        f = open(SSH_CONFIG_FILE_LOC, 'a')
    else:
        f = open(SSH_CONFIG_FILE_LOC, 'w')
    f.write("Host {0}\n".format(host))
    f.write("\tHostName {0}\n".format(hostname))
    f.write("\tUser {0}\n".format(user))
    if port:
        f.write("\tPort {0}\n".format(port))
    if identityfile:
        f.write("\tIdentityFile {0}\n".format(identityfile))
    f.close()

if __name__ == '__main__':
    create_config()
    print(get_config())
