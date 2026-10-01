# Write an unit test for the directory_tree script
from operations.directory_tree import print_directory_tree

def test_print_directory_tree(tmp_path):
    # Create a sample directory structure
    (tmp_path / "dir1").mkdir()
    (tmp_path / "dir1" / "file1.txt").write_text("content1")
    (tmp_path / "dir2").mkdir()
    (tmp_path / "dir2" / "file2.txt").write_text("content2")

    # Capture the printed output
    from io import StringIO
    import sys

    captured_output = StringIO()
    sys.stdout = captured_output
    print_directory_tree(str(tmp_path))
    sys.stdout = sys.__stdout__

    output = captured_output.getvalue()
    assert "dir1" in output
    assert "file1.txt" in output
    assert "dir2" in output
    assert "file2.txt" in output
