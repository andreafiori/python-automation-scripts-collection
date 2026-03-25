import os
import tempfile
import pytest

from app.file_management.tree_generator import directory_tree

@pytest.fixture
def sample_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create sample structure
        os.makedirs(os.path.join(tmpdir, "subdir1"))
        os.makedirs(os.path.join(tmpdir, "subdir2"))
        with open(os.path.join(tmpdir, "file1.txt"), "w") as f:
            f.write("test")
        with open(os.path.join(tmpdir, "subdir1", "file2.txt"), "w") as f:
            f.write("test")
        yield tmpdir

def test_directory_tree(sample_dir):
    result = directory_tree(sample_dir)
    assert "file1.txt" in result
    assert "subdir1" in result
    assert "file2.txt" in result
    assert "subdir2" in result

def test_nonexistent_directory():
    result = directory_tree("/nonexistent/path")
    assert "[Directory not found" in result

def test_permission_denied(monkeypatch):
    def mock_listdir(path):
        raise PermissionError
    monkeypatch.setattr(os, "listdir", mock_listdir)
    result = directory_tree("/some/path")
    assert "Permission denied" in result
