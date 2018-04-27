"""
Jeffery Russell
4-27-18
"""

import subprocess
import collections

import module
import configuration


"""
The mounts.txt file is a sequence of three strings

user@remote.server.address
/remote/mount/point
/local/mount/point
"""
MOUNT_FILE = configuration.get_config().mounts


def add_drive_to_config(remote_connection, remote_mount_point, local_mount_point):
    """
    Adds a new network drive to the default mount config file
    """
    module.append_file(MOUNT_FILE, remote_connection)
    module.append_file(MOUNT_FILE, remote_mount_point)
    module.append_file(MOUNT_FILE, local_mount_point)


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
    with open(MOUNT_FILE) as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            mount_drive(lines[i], lines[i + 1], lines[i + 2])
            i+=3


def unmount_drive(local_mount_point):
    """
    UnMounts a drive from a computer
    """
    subprocess.call(["umount", local_mount_point])


def unmount_drives():
    """
    UnMounts the ssh drives from the computer
    """
    with open(MOUNT_FILE) as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            unmount_drive(lines[i + 2])
            i+=3


def print_usage():
    """
    Prints the usage message to the terminal
    """
    print("Usage -m, or -u")
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
            unmount_drives()
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
        exit_program()