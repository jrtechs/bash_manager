#!/bin/bash
# virtualenv-auto-activate.sh
# 
# Installation:
#   Add this line to your .bashrc or .bash-profile:
#
#       source /path/to/virtualenv-auto-activate.sh
#
#   Go to your project folder, run "virtualenv .venv", so your project folder
#   has a .venv folder at the top level, next to your version control directory.
#   For example:
#   .
#   ├── .git
#   │   ├── HEAD
#   │   ├── config
#   │   ├── description
#   │   ├── hooks
#   │   ├── info
#   │   ├── objects
#   │   └── refs
#   └── .venv
#       ├── bin
#       ├── include
#       └── lib
#
#   The virtualenv will be activated automatically when you enter the directory.
_virtualenv_auto_activate() {
    if [ -e ".venv" ]; then
        # Check to see if already activated to avoid redundant activating
        if [ "$VIRTUAL_ENV" != "$(pwd -P)/.venv" ]; then
            _VENV_NAME=$(basename `pwd`)
            echo Activating virtualenv \"$_VENV_NAME\"...
            VIRTUAL_ENV_DISABLE_PROMPT=1
            source .venv/bin/activate
            _OLD_VIRTUAL_PS1="$PS1"
            PS1="($_VENV_NAME)$PS1"
            export PS1
        fi
    fi
}

export PROMPT_COMMAND=_virtualenv_auto_activate

