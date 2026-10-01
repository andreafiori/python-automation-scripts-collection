"""
Create a script that return a directory tree structure in a readable format
"""

import os

def print_directory_tree(path: str, prefix: str = "") -> None:
    # Get the list of files and directories in the given path
    entries = os.listdir(path)
    entries.sort()  # Sort entries for consistent output

    for index, entry in enumerate(entries):
        entry_path = os.path.join(path, entry)
        is_last = index == len(entries) - 1  # Check if it's the last entry

        # Print the current entry with the appropriate prefix
        print(prefix + ("└── " if is_last else "├── ") + entry)

        # If the entry is a directory, recursively print its contents
        if os.path.isdir(entry_path):
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_directory_tree(entry_path, new_prefix)
