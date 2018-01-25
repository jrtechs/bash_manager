# roosay
````   
-------------
< Only at RIT >
-------------

          \    /)/)
           \  (ø.ø)
               \ (    />
             __/ _\  //
            '~( '~ )//
              _\  '}/
             "--~(/
````

roosay is a simple python script which displays an ascii roo with a quote above it

## Install
 Copy the roosay.py file from the src directory

## Usage

   python3 roosay.py Super cool message

or create a .bashrc alias

   roosay super cool message

# SSH Manager
````
**************************************
*         SSH manager V 0.2          *
* 1) user1@host_name                 *
* 2) user2@host_name_2               *
* A) Exit                            *
* B) Manager tools                   *
* C) Socks Tunnel                    *
**************************************
````

## About
I developed this program to simply make it easier to manager all your ssh accounts
in a single program. SSH keys are nice; however, you still have type "ssh user1@host"
every time you wish to connect to a computer -- which can be a lot for some people.
This program keeps track of all your ssh accounts so they are a few keystrokes away.

## Installation
This program is simply a python script that you execute. For example:

    python3 ssh_manager.py
  
or edit your bash configuration with an alias to make it less typing

   alias ss="python3 /path/to/this/file/ssh_manager.py"
  
Please note that this program reads in a text file called "servers.txt". In order for
the bash manager to know where this text file is, please edit line 11 of ssh_manager.py
it should look something like this:

   INPUT_FILE = "/path/to/servers.txt"
  
## Usage
Your first time running you should see:
````
**************************************
*         SSH manager V 0.2         *
* A) Exit                            *
* B) Manager tools                   *
* C) Socks Tunnel                    *
**************************************
````
I would like to believe that I made this menu intuitive enough so you don't have to
read any documentation. However...

Typing B will pull up this menu:

````
**************************************
* Options                            *
* 1) Add Host                        *
* 2) Copy SSH key to server          *
* 3) Remove host name                *
* 4) Return to ssh manager           *
* 5) Exit                            *
**************************************
Enter selection:
````
This is where you can run the add host names to the manager -- same as adding them to
the "servers.txt".

If you don't have ssh keys installed on your servers, or forgot the command to do so,
you can use the "2" option to copy your ssh key to a server.

"3" Pulls up an additional menu which you can use to select a entry to remove.

"4" Returns to the main manager window.

If you added some accounts your main window should look like this:

````
**************************************
*         SSH manager V 0.2          *
* 1) user1@host_name                 *
* 2) user2@host_name_2               *
* A) Exit                            *
* B) Manager tools                   *
* C) Socks Tunnel                    *
**************************************
````

Now is the easy part. Simply enter the number of the computer you wish to connect to
and it will open a ssh connection.

If you are interested in doing lots of socks proxies -- for whatever reason.
From the main menu type "C".

````
**************************************
*         Socks Tunnel               *
* 1) user1@host_name                 *
* 2) user2@host_name_2               *
* A) Exit                            *
* B) Main                            *
**************************************
````

Now whichever computer you select, it will open a socks proxy. To use the proxy use
localhost and port 8123.



