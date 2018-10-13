#! /usr/bin/bash

#Created by Jake Zaia

#Takes in one argument, a commit message, and handles the entire git workflow.

git pull;
git add .;
git commit -am "$1";
git push;
