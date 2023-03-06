#!/bin/bash

# Prompt user for file name to search for
read -p "Enter file name to search for: " filename

# Prompt user for directory to search in
read -p "Enter directory to search in (default is current directory): " directory

# If no directory is provided, use current directory
if [ -z "$directory" ]; then
    directory="."
fi

# Search for files in directory and its subdirectories
result=$(find "$directory" -name "*$filename*" -print)

# If files are found, print the directory paths
if [ -n "$result" ]; then
    echo "Files found in directories:"
    echo "$result"
else
    echo "No files found in directory"
fi
