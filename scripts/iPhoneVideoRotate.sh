#!/bin/sh

# This script rotates video files that were created on an iPhone,
# but being edited on Linux. Requires the CLI version of HandBrake.

# This script takes two arguments:
# First argument is the input file
# Second argument is the output file 

HandBrakeCLI --rotate=4 --preset "High Profile" -O -i $1 -o $2
