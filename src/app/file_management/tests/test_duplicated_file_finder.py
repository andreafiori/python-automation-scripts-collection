"""
Tests for the DuplicatedFilesFinder class using mock objects to simulate file system interactions.
"""

from operations.duplicated_files_finder import DuplicatedFilesFinder
from unittest.mock import patch, MagicMock

@patch("operations.duplicated_files_finder.os.walk")
def test_find_duplicates(mock_os_walk):
    # Mock the os.walk to simulate a directory structure
    mock_os_walk.return_value = [
        ("root", ("subdir",), ("file1.txt", "file2.txt", "file3.txt")),
    ]

    finder = DuplicatedFilesFinder()
    duplicates = finder.find_duplicates("root")

    # Check that duplicates are found correctly
    assert "root/file1.txt" in duplicates
    assert "root/file2.txt" in duplicates
    assert "root/file3.txt" not in duplicates
