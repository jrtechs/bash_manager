"""
Jeffery Russell
4-27-18

Deals with the configuration file for bash manager

Config file:
servers: /path/to/servers
quotes: /path/to/quotes.txt
forward: /path/to/forwards.txt
mounts: /path/to/ssh/mounts.txt


config dictionary
{servers: "/", quotes: "/", forwards: "/", mounts:"/"}
"""

import os.path

from utils import module

CONFIG_FILE = os.path.dirname(__file__) + "/config.txt"


def config_exists():
    """
    Function which checks to see if the config file exists
    :return: whether file returns
    """
    if not os.path.exists(CONFIG_FILE):
        print("config file not found in " + CONFIG_FILE)
        return False
    return True


def single_conf_input(param):
    """
    helper function for create_config() which reads the value of a single
    file location from the user
    """
    print("\nPlease enter the absolute path for your " + param + " file if you leave this blank,")
    print("by default it will be "  
        + os.path.dirname(__file__) + "/" + param + ".txt")
    i = input("Enter selection:")
  
    if i.strip() == "":
        return  param + ": " + os.path.dirname(__file__) + "/" + param + ".txt"
    else:
        return param + ": " + i


def create_config():
    """
    Creates a new configuration file
    """
    print("Creating new configuration file under " + CONFIG_FILE)

    f = open(CONFIG_FILE, "w")
    f.write(single_conf_input("servers") + '\n')
    f.write(single_conf_input("quotes") + '\n')
    f.write(single_conf_input("forwards")+ '\n')
    f.write(single_conf_input("mounts") + '\n')
    f.close()


def read_config():
    """
    Reads the config file and creates a config dictionary
    """
    config = {}
    with open(CONFIG_FILE) as file:
        for line in file:
            temp = line.split(" ")

            if len(temp) >= 1:
                temp[1] = temp[1].strip('\n')

            if line.find("servers:") != -1:
                if len(temp) <= 1:
                    print("Error reading servers file from config")
                    return
                config["servers"] = temp[1]
            if line.find("quotes:") != -1:
                if len(temp) <= 1:
                    print("Error reading quotes file from config")
                    return
                config["quotes"] = temp[1]

            if line.find("forwards:") != -1:
                if len(temp) <= 1:
                    print("Error reading forwards file from config")
                    return
                config["forwards"] = temp[1]
            if line.find("mounts:") != -1:
                if len(temp) <= 1:
                    print("Error reading mounts file from config")
                    return
                config["mounts"] = temp[1]
    return config


def valid_config(config):
    """
    Checks to see if a configuration is valid
    """
    return 'servers' in config and 'quotes' in config and 'forwards' in config and 'mounts' in config


def create_config_dependent_files(config):
    """
    Finds missing files and creates them
    """
    if os.path.isfile(config["servers"]) == False:
        print("Creating missing servers file in " + config["servers"])
        module.create_empty_file(config["servers"])
    if os.path.isfile(config["quotes"]) == False:
        print("Creating missing quotes file in " + config["quotes"])
        module.create_empty_file(config["quotes"])
    if os.path.isfile(config["forwards"]) == False:
        print("Creating missing forwards file in " + config["forwards"])
        module.create_empty_file(config["forwards"])
    if os.path.isfile(config["mounts"]) == False:
        print("Creating missing mounts file in " + config["mounts"])
        module.create_empty_file(config["mounts"])


def get_config():
    """
    Returns the config file for the main to use
    """
    if not config_exists():
        module.create_empty_file(CONFIG_FILE)
        create_config()
    config = read_config()

    if valid_config(config):
        create_config_dependent_files(config)
        
        return config
    else:
        create_config()
        return get_config()


def generate_bash_aliases():
    """
    Generates the bash aliases to add to the bash congig
    :return: list of strings with bash aliases
    """
    aliases = []
    path = os.path.dirname(os.path.abspath(__file__)) + "/"
    aliases.append("alias roosay=\"python3 " + path + "roosay.py\"")
    aliases.append("alias ss=\"python3 " + path + "ssh_manager.py\"")
    aliases.append("alias ssh_manager=\"python3 " + path + "ssh_manager.py\"")
    aliases.append("alias mm=\"python3 " + path + "mount_ssh_drive.py\"")
    aliases.append("alias ssh-mount=\"python3 " + path + "mount_ssh_drive.py\"")
    aliases.append("alias quote=\"python3 " + path + "quote.py\"")

    return aliases


def generate_extra_sauce():
    """
    Creates a list of bash configurations things that I use
    :return: string list with all my extra bash sauce
    """
    sauce = []

    sauce.append("alias ls=\"ls -abp --color=auto\"")
    sauce.append("function cd {")
    sauce.append("\tbuiltin cd \"$@\" && ls")
    sauce.append("}")
    sauce.append("quote")

    return sauce


def view_shell_sauce():
    """
    Displays the output of generate_bash_aliases() and generate_extra_sauce()
    """
    print("\n#Bash Aliases:")

    for line in generate_bash_aliases():
        print(line)

    print("\n")
    print("#Extra Sauce")

    for line in generate_extra_sauce():
        print(line)


def write_to_bash_config(sauce):
    """
    prompts user for name of shell config file and write contents of
    sauce to it
    """
    path = input("Enter name of shell (.bashrc or .zshrc):")
    path = "~/" + path

    for line in sauce:
        module.append_file(path, line)

    print("Added the following to " + path)

    for line in sauce:
        print("\t" + line)


def main():
    """
    Prompts user to either update the config file, or make aliases
    in the bash configuration
    """

    options = []
    options.append("1) Update Configuration File")
    options.append("2) Make Aliases")
    options.append("3) Add Extra Sauce")
    options.append("4) View proposed shell conf")
    options.append("5) Exit")
    i = '0'

    while i != '5':
        module.print_menu("Configuration Manager", options)
        i = input("Enter Option:")
        if i == '1':
            create_config()
        elif i == '2':
            write_to_bash_config(generate_bash_aliases())
        elif i == '3':
            write_to_bash_config(generate_extra_sauce())
        elif i == '4':
            view_shell_sauce()


"""
Makes sure that other programs don't execute the main
"""
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
