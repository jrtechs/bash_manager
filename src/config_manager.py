"""
Jake Zaia
2018-10-12

Manages SSH config files, and supports a more user-friendly terminal based way of creating them
"""

import os

#This is the location of where the SSH
SSH_CONFIG_FILE_LOC = os.path.expanduser('~/.ssh/config')
bar = '================================\n'


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

def get_entries():
    """
    Creates a list of dictionaries where each dictionary contains all the information about a Host in the SSH config.
    """
    ret = []
    config = get_config().split('\n')

    #Operate on each line in the config
    for i in range(len(config)):
        #Add a new host entry
        if config[i][0:4] == 'Host':
            ret.append({})
            ret[-1]['Host'] = config[i][5:]

        #Add information to the current host
        if "\t" in config[i]:
            config[i] = config[i].strip()
            key = config[i][0: config[i].find(' ')]
            value = config[i][1 + config[i].find(' '):]
            ret[-1][key] = value
    return ret

def print_entry_info(entry):
    """
    Conveniently displays the information for one entry in the SSH Config
    Takes a dictionary as input.
    """
    print("Host: {0}".format(entry['Host']))
    print("HostName: {0}".format(entry['HostName']))
    print("User: {0}".format(entry['User']))

    #Optional
    if 'Port' in entry:
        print("Port: {0}".format(entry['Port']))
    if 'IdentityFile' in entry:
        print("IdentityFile: {0}".format(entry['IdentityFile']))

def modify_entry():
    """
    Gets all current entries and allows the user to modify the current values.
    """
    entries = get_entries()
    print("Which entry would you like to modify?")
    for i in range(len(entries)):
        print("{0}: {1}".format(i, entries[i]['Host']))
    i = int(input())

    #Print to ensure the correct property is specified
    print_entry_info(entries[i]);
    prop = input("Which property would you like to edit? (case sensitive) ")
    value = input("What should the new value be? ")
    entries[i][prop] = value

    #Update actual file
    push_config(entries)
    print("Successfully updated the entry.")

def remove_entry():
    """
    Facilitates removing a singular entry from the SSH Config file
    """
    entries = get_entries()
    print("Which entry would you like to remove?")
    for i in range(len(entries)):
        print("{0}: {1}".format(i, entries[i]['Host']))
    i = int(input())
    print(bar)

    #For safety
    print_entry_info(entries[i]);
    resp = input("Really delete this entry? [y/N] ")
    if (resp=='y' or resp=='Y' or resp.lower() == 'yes'):
        entries.pop(i)
        print("Successfully deleted.")
    push_config(entries)

def push_config(config):
    """
    Overwrites current config with an input list of dictionaries. Used as a helper to modify values in the SSH Config.
    """
    f = open(SSH_CONFIG_FILE_LOC, 'w')
    for each in config:
        f.write("Host {0}\n".format(each['Host']))
        f.write("\tHostName {0}\n".format(each['HostName']))
        f.write("\tUser {0}\n".format(each['User']))
        if 'Port' in each:
            f.write("\tPort {0}\n".format(each['Port']))
        if 'IdentityFile' in each:
            f.write("\tIdentityFile {0}\n".format(each['IdentityFile']))
    f.close()

def create_entry():
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
    print("Successfully created the entry.")

if __name__ == '__main__':
    cont = True
    while(cont):
        print("Modify your SSH Config file. Please Select an option:")
        print("0: Add a new entry")
        print("1: List all information")
        print("2: Modify an existing entry")
        print("3: Remove an entry")
        print("Any other number: exit")
        resp = input()
        print(bar)
        if resp == '0':
            create_entry()
        elif resp == '1':
            for each in get_entries():
                print()
                print_entry_info(each)
        elif resp == '2':
            modify_entry()
        elif resp == '3':
            remove_entry()
        else:
            cont = False
        print(bar)
