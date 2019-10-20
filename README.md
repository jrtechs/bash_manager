# Roosay

```

 /-----------\
< Only at RIT >
 \-----------/

          \    /)/)
           \  (ø.ø)
               \ (    />
             __/ _\  //
            '~( '~ )//
              _\  '}/
             "--~(/
```

roosay is a simple python script which displays an ascii roo with a quote above it

## Usage
```
python3 roosay.py Super cool message
```
or create a .bashrc alias
```
roosay super cool message
```

# Install
Use git to clone this project onto your system. A one-command installation can be done using the `git clone` 
```
git clone https://github.com/jrtechs/bash_manager.git
```


# Dependencies
Make sure that you have the following programs installed.
- python3
- ssh
- ssh-copy-id
- sshfs (only for ssh drive manager)
- fusermount (only for ssh drive manager)


# SSH Manager
```
**************************************
*         SSH manager V 1.1          *
* 1) user1@host_name                 *
* 2) user2@host_name_2               *
* A) Exit                            *
* B) Manager tools                   *
* C) Socks Tunnel                    *
* D) SSH Drive Manager               *
**************************************
```

## About
I developed this program to simply make it easier to manager all your ssh accounts
in a single program. SSH keys are nice; however, you still have type "ssh user1@host"
every time you wish to connect to a computer -- which can be a lot for some people.
This program keeps track of all your ssh accounts so they are a few keystrokes away.

## Installation
This program is simply a python script that you execute.
```
python3 ssh_manager.py
```
  
You can edit your bash configuration with an alias to make it easier to execute.
```
alias ss="python3 /path/to/this/file/ssh_manager.py"
```

To make this easier, the configuation manager of this program will has the option to
append this and a few other aliases to your bash manager. This will automatically
use the location of the scripts in the file.
  
The first time you run this program it will ask you for the locations where you want to store
some files which will be used to store the host names and user accounts. The default is to put
it in the same directory as the source code.


## Usage
After you accept the configuration you will see something like this.
````
**************************************
*         SSH manager V 1.1          *
* A) Exit                            *
* B) Manager tools                   *
* C) Socks Tunnel                    *
* D) SSH Drive Manager               *
**************************************

**************************************
````
I would like to believe that I made this menu intuitive enough so you don't have to
read any documentation. However...

Typing B will pull up this menu:

````
 **************************************
 *              Options               *
 * 1) Add Host                        *
 * 2) Copy SSH key to server          *
 * 3) Remove host name                *
 * 4) Return to ssh manager           *
 * 5) Manage Configuration and Bash   *
 * 6) Exit                            *
 **************************************
Enter selection:
````
This is where you can run the add host names to the manager -- same as adding them to
the "servers.txt".

If you don't have ssh keys installed on your servers, or forgot the command to do so,
you can use the "2" option to copy your ssh key to a server.

"3" Pulls up an additional menu which you can use to select a entry to remove.

"4" Returns to the main manager window.

"5" Edits the configuration which stores where this program keeps text documents
for the hosts used.

If you added some accounts your main window should look like this:

````
**************************************
*         SSH manager V 1.1          *
* 1) user1@host_name                 *
* 2) user2@host_name_2               *
* A) Exit                            *
* B) Manager tools                   *
* C) Socks Tunnel                    *
* D) SSH Drive Manager               *
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


# SSH Drive Mount Manager

This manager makes it easier to mount ssh drives using the "fusermount" command.

```
 **************************************
 *         SSH Drive Manager          *
 * 1) Mount SSH Drives                *
 * 2) Un-Mount SSH Drives             *
 * 3) Remove Remote Drive             *
 * 4) Add Drive to Mount              *
 * 5) View Drives                     *
 * 6) Usage                           *
 * 7) Manage Config                   *
 * 8) Exit                            *
 **************************************
```

#  Benifits

This SSH manager will help to manage everything easily without any fails.
