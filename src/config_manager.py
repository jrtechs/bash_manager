#This file manages SSH config files

SSH_CONFIG_FILE_LOC = 'config'

def create_config():
    print("Please input the relevent information for generating your config file.")
    host = input("Nickname for Host: ")
    hostname = input("Hostname: ")
    user = input("Username: ")
    port = input("Would you like to specify a port?(y/N)")
    if (port == 'y' or port == 'Y' or port.lower() =='yes'):
        port = input("Port number: ")
    else:
        port = None
    identityfile = input("Would you like to specify an ssh key location?(y/N)")
    if (identityfile == 'y' or identityfile == 'Y' or identityfile.lower() =='yes'):
        identityfile = input("SSH Public key file location: ")
    f = open(SSH_CONFIG_FILE_LOC, 'w')
    f.write("Host {0}\n".format(host))
    f.write("\tHostName {0}\n".format(hostname))
    f.write("\tUser {0}\n".format(user))
    if port:
        f.write("\tPort {0}\n".format(port))
    if identityfile:
        f.write("\tIdentityFile {0}\n".format(identityfile))

create_config()