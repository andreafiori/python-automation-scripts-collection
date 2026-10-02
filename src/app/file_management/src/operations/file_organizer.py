import os
import shutil


"""
A simple utility for organizing files in a specified directory. It automatically sorts files into subdirectories based on their file extensions, making it easier to manage and locate files.

Features
Automatic Organization: Files are moved into subfolders named after their extensions (e.g., all .jpg files go into a folder named jpg).
Dynamic Folder Creation: If a folder for a specific file type doesn't exist, it will be created automatically.

Usage
- Open a terminal or command prompt and navigate to the directory where the script is located
- Run the script using the following command: python FileOrganizer.py
- When prompted, enter the path of the directory you want to organize. Enter path: /path/to/your/directory
- The script will process the files in the specified directory and create folders for each file type, moving the corresponding files into their respective folders

"""

class FileOrganizer:

    def organize_files(self, path: str):
        # Check if the directory exists
        if not os.path.exists(path):
            print("Error: The specified directory does not exist.")
        else:
            # List all items in the specified directory
            files = os.listdir(path)

            # Iterate through each file in the directory
            for file in files:
                file_path = os.path.join(path, file)

                # Skip directories
                if os.path.isdir(file_path):
                    continue

                # Split the filename and extension
                filename, extension = os.path.splitext(file)
                extension = extension[1:] if extension else "NoExtension"  # Handle files without extensions

                # Destination folder for the extension
                dest_folder = os.path.join(path, extension)

                # Create the directory if it does not exist
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)

                # Handle duplicate files by renaming them
                dest_file_path = os.path.join(dest_folder, file)
                counter = 1
                while os.path.exists(dest_file_path):
                    new_filename = f"{filename}{counter}.{extension}" if extension != "NoExtension" else f"{filename}_{counter}"
                    dest_file_path = os.path.join(dest_folder, new_filename)
                    counter += 1

                # Move the file
                shutil.move(file_path, dest_file_path)
                print(f"Moved: {file} → {dest_file_path}")
