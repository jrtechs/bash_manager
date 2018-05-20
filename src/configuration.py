"""
Jeffery Russell
4-27-18

Deals with the configuration file for bash manager

Config file:
servers: /path/to/servers
quotes: /path/to/quotes.txt
mounts: /path/to/ssh/mounts.txt


config dictionary
{servers: "/", quotes: "/", mounts:"/"}
"""

import subprocess
import collections
import os.path

import module

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
    f.write(single_conf_input("mounts") + '\n')
    f.close()


def read_config():
    """
    Reads the config file and creates a config dictionary
    """
    config = {}
    temp = []
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
    return 'servers' in config and 'quotes' in config and 'mounts' in config

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

        



