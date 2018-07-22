#!/bin/bash

# Simple script for optimizing all images for a website
#
# @author Jeffery Russell 7-19-18

WIDTH="690>"  # the ">" tag specifies that images will not get scaled up

for f in $(find "./" -name '*.jpg' -or -name '*.JPG'); do
    convert "$f" -resize $WIDTH "$f"
    jpegoptim --max=80 --strip-all --preserve --totals --all-progressive "$f"
done

for f in $(find "./" -name '*.png' -or -name '*.PNG'); do
    convert "$f" -resize $WIDTH "$f"
    optipng -o7 -preserve "$f"
done