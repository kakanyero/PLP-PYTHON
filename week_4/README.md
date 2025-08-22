
# WEEK 4
# Overview

This project is a simple Python script that reads a file, modifies its content, and writes the modified version to a new file. The script is designed to handle errors and exceptions that may occur during file reading and writing.

# Features

- Reads a file specified by the user
- Modifies the content of the file (converts to uppercase)
- Writes the modified content to a new file
- Handles errors and exceptions during file reading and writing

# Requirements

- Python 3.x

# Usage

1. Save the script to a file (e.g., `week_4.py`)
2. Create a file named `movies.txt` with some content
3. Run the script using Python (e.g., `python file_modifier.py`)
4. Enter the filename `movies.txt` when prompted
5. The script will create a new file named `modified_movies.txt` with the modified content

# Error Handling

The script handles the following errors:

- `FileNotFoundError`: Raised when the file does not exist
- `PermissionError`: Raised when you do not have permission to read the file
- `Exception`: A catch-all for any other unexpected errors

# Notes

- The script assumes that the file is in the same directory as the script. If the file is in a different directory, you need to specify the full path to the file.
- The script overwrites any existing file with the same name as the outpuit file.
