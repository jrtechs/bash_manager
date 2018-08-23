"""
Jeffery Russell
4-27-18
"""

import subprocess
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
    runCode = subprocess.call(["fusermount", "-u", local_mount_point])

    if runCode == 0:
        print("Un-Mounted " + local_mount_point)
    else:
        print("Failed to Un-Mount " + local_mount_point)


def unmount_all_drives():
    """
    UnMounts the ssh drives from the computer
    """
    file = module.input_file(MOUNT_FILE)
    for i in range(0, len(file), 3):
        unmount_drive(file[i + 2])


def remove_drive():
    """
    Prompts the user and removes a drive from MOUNT_FILE
    """
    options = []
    file = module.input_file(MOUNT_FILE)
    for i in range(0, len(file), 3):
        options.append(str(len(options) + 1) + ") " + file[i])
    
    options.append("A) Exit")

    module.print_menu("Remove SSH Drive", options)

    i = input("Enter Option:")

    if i.lower() != 'a' and int(i) <= len(file)/3 and int(i) > 0:
        index = (int(i) - 1) * 3

        f = open(MOUNT_FILE, "w")
        for x in range(0, len(file), 3):
            if index != x:
                f.write(file[x] + "\n")
                f.write(file[x + 1] + "\n")
                f.write(file[x + 2] + "\n")
        f.close()


def add_drive_to_config(remote_connection, remote_mount_point,
                        local_mount_point):
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


def view_drives():
    """
    Views the current drives to the user
    """
    drives = []
    file = module.input_file(MOUNT_FILE)
    for i in range(0, len(file), 3):
        drives.append(str(int(int(i)/3 + 1)) + ") " + file[i])
        drives.append("   " + file[i + 1])
        drives.append("   " + file[i + 2])
    module.print_menu("SSH Drives", drives)


def print_mount_menu():
    """
    Displays box which has mount menu options
    """
    module.print_menu("SSH Drive Manager", ["1) Mount SSH Drives",
                                            "2) Un-Mount SSH Drives",
                                            "3) Remove Remote Drive",
                                            "4) Add Drive to Mount",
                                            "5) View Drives",
                                            "6) Usage",
                                            "7) Manage Config",
                                            "8) Exit"])


def manage_mount_file():
    """
    Method which prompts user which action to take with mounts file
    """
    print_mount_menu()
    i = input("Enter Option:")
    while i != '8':
        if i == '4':
            add_drive()
        elif i == '3':
            remove_drive()
        elif i == '5':
            view_drives()
        elif i == '1':
           mount_drives()
        elif i == '2':
            unmount_all_drives()
        elif i == '6':
            print_usage()
        elif i == '7':
            configuration.main()
        else:
            print("Invalid Option")
        if i != '1' and i != '2':
            print_mount_menu()
            i = input("Enter Option:")
        else:
            break


def print_usage():
    """
    Prints the usage message to the terminal
    """
    print("Usage:")
    print("\t-m mounts drives to computer")
    print("\t-u unmounts drives from the computer")


def main():
    """
    Parses cmd line input and calls appropriate functions
    """
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "-m":
            mount_drives()
        elif sys.argv[1].lower() == "-u":
            unmount_all_drives()
        else:
            print("Invalid Command")
            print_usage()
    else:
        manage_mount_file()


"""
Makes sure that other programs don't execute the main
"""
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()