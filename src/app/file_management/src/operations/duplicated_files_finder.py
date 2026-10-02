import os

from pathlib import Path
from filecmp import cmp

"""
Find duplicated files recursively in a directory.
"""
class DuplicatedFilesFinder:

    def find_duplicates(self, directory: str):
        file_map = {}
        duplicated_files = []

        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                if file in file_map:
                    duplicated_files.append(file_path)
                else:
                    file_map[file] = file_path

        return duplicated_files

    def filecmp_solution(self, directory: str):
        # list of all documents
        data_dir = Path(directory)
        files = sorted(os.listdir(data_dir))

        duplicated_files = []

        # comparison of the documents
        for file_x in files:

            if_dupl = False

            for class_ in duplicated_files:
                # Comparing files having same content using cmp()
                # class_[0] represents a class having same content
                if_dupl = cmp(
                    data_dir / file_x,
                    data_dir / class_[0],
                    shallow=False
                )
                if if_dupl:
                    class_.append(file_x)
                    break

            if not if_dupl:
                duplicated_files.append([file_x])

        return duplicated_files