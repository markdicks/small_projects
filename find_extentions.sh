#!/bin/bash

# Prompt the user for the file extension to search for
read -p "Enter the file extension to search for (e.g. txt, py, etc): " ext

# Find all files with the specified extension in the current directory and subdirectories
files=$(find . -type f -name "*.$ext")

# Check if any files were found
if [ -z "$files" ]; then
    echo "No files with extension .$ext found in the current directory and subdirectories."
else
    # Print the file paths of the found files
    echo "The following files with extension .$ext were found in the current directory and subdirectories:"
    echo "$files"
fi
