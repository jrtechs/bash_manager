#!/bin/bash

# ANSI color setup

#use printf or echo -e

defineANSI() {

esc="\e"
# esc="\033"

# Foreground colors
	FBLACK="${esc}[30m"
	FRED="${esc}[31m"
	FGREEN="${esc}[32m"
	FYLLW="${esc}[33m"
	FBLUE="${esc}[34m"
	FPRPL="${esc}[35m"
	FCYAN="${esc}[36m"
	FWHITE="${esc}[37m"

# Background colors
	BBLACK="${esc}[40m"
	BRED="${esc}[41m"
	BGREEN="${esc}[42m"
	BYLLW="${esc}[43m"
	BBLUE="${esc}[44m"
	BPRPL="${esc}[45m"
	BCYAN="${esc}[46m"
	BWHITE="${esc}[47m"

# Bold, italic, underline, and inverse style toggles
	BOLDON="${esc}[1m"
	BOLDOFF="${esc}[22m"
	ITALON="${esc}[3m"
	ITALOFF="${esc}[23m"
	UNDERON="${esc}[4m"
	UNDEROFF="${esc}[24m"
	BLINK="${esc}[5m"
	STATIC="${esc}[25m"
	INVON="${esc}[7m"
	INVOFF="${esc}[27m"
	RESET="${esc}[0m"

}

echo $RESET
