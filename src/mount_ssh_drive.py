"""
Jeffery Russell
4-27-18
"""

import subprocess
import collections
import sys

import module
import configuration


"""
The mounts.txt file is a sequence of three strings

user@remote.server.address
/remote/mount/point
/local/mount/point
"""
MOUNT_FILE = configuration.get_config()["mounts"]


def mount_drive(remote_connection, remote_mount_point, local_mount_point):
    """
    Calls sshfs to mount a remote connection on a local mount point over ssh
    """
    runCode = subprocess.call(["sshfs", "-o", "allow_other", 
            remote_connection + ":" + remote_mount_point, local_mount_point])
    if runCode == 0:
        print("Mounted "  + remote_connection + ":" + remote_mount_point + 
            " to " + local_mount_point)
    else:
        print("Failed to mount " + remote_connection + ":" + remote_mount_point)


def mount_drives():
    """
    Mounts all the ssh drives in the configuration file
    """
    file = module.input_file(MOUNT_FILE)
    if len(file) == 0:
        print(MOUNT_FILE + " is empty")
    else:
        for i in range(0, len(file), 3):
            mount_drive(file[i], file[i + 1], file[i + 2])


def unmount_drive(local_mount_point):
    """
    UnMounts a drive from a computer
    """
    subprocess.call(["fusermount", "-u", local_mount_point])


def unmount_all_drives():
    """
    UnMounts the ssh drives from the computer
    """
    file = module.input_file(MOUNT_FILE)
    for i in range(0, len(file), 3):
        unmount_drive(file[i + 2])


def remove_drive():
    """

    """
    options = []
    file = module.input_file(MOUNT_FILE)
    for i in range(0, len(file), 3):
        options.append(str(len(options) + 1) + ") " + file[i])
    
    options.append("A) Exit")

    module.print_menu("SSH Drive Manager", options)


def add_drive_to_config(remote_connection, remote_mount_point, local_mount_point):
    """
    Adds a new network drive to the default mount config file
    """
    module.append_file(MOUNT_FILE, remote_connection)
    module.append_file(MOUNT_FILE, remote_mount_point)
    module.append_file(MOUNT_FILE, local_mount_point)


def add_drive():
    """
    Prompts the user to enter information to add ssh mount drive to config
    """
    ssh_acct = input("Enter your ssh account:")
    remote_mount = input("Enter the remote mount point:")
    local_mount = input("Enter the local mount point:")
    add_drive_to_config(ssh_acct, remote_mount, local_mount)


def print_mount_menu():
    """
    Displays box which has mount menu options
    """
    module.print_menu("SSH Drive Manager", ["1) Remove Remote Drive",
                                            "2) Add Drive to Mount",
                                            "3) Exit"])


def manage_mount_file():
    """
    Method which prompts user which action to take with mounts file
    """
    print_mount_menu()
    i = input("Enter Option:")
    while i != '3':
        if i == '2':
            add_drive()
        elif i == '1':
            remove_drive()
        else:
            print("Invalid Option")
        print_mount_menu()
        i = input("Enter Option:")


def print_usage():
    """
    Prints the usage message to the terminal
    """
    print("Usage:")
    print("\t-m mounts drives to computer")
    print("\t-u unmounts drives from the computer")
    print("\t-e manages config file with drives to mount")


def main():
    """
    Parses cmd line input and calls appropriate functions
    """
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "-m":
            mount_drives()
        elif sys.argv[1].lower() == "-u":
            unmount_all_drives()
        elif sys.argv[1].lower() == "-e":
            manage_mount_file()
        else:
            print_usage()
    else:
        print_usage()


"""
Makes sure that other programs don't execute the main
"""
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()