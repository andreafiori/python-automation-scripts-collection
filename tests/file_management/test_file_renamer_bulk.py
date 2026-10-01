from app.file_system.file_renamer_bulk import bulk_rename


def test_bulk_rename_dry_run(tmp_path):
    # Create test files in a temporary directory
    file1 = tmp_path / "Screenshot 2026-03-01 at 12.00.00.png"
    file1.write_text("dummy content 1")
    file2 = tmp_path / "ignore_me.txt"
    file2.write_text("dummy content 2")

    pattern = r"Screenshot (\d{4})-(\d{2})-(\d{2}) at .+\.png"
    replacement = r"\1\2\3_capture.png"

    renamed = bulk_rename(str(tmp_path), pattern, replacement, dry_run=True)

    # Check return value captures the expected change
    assert renamed == [
        ("Screenshot 2026-03-01 at 12.00.00.png", "20260301_capture.png")
    ]

    # Verify original file still exists and no new file was created (dry run)
    assert file1.exists()
    assert not (tmp_path / "20260301_capture.png").exists()
    assert file2.exists()


def test_bulk_rename_execution(tmp_path):
    file1 = tmp_path / "Screenshot 2026-03-01 at 12.00.00.png"
    file1.write_text("dummy content 1")

    pattern = r"Screenshot (\d{4})-(\d{2})-(\d{2}) at .+\.png"
    replacement = r"\1\2\3_capture.png"

    renamed = bulk_rename(str(tmp_path), pattern, replacement, dry_run=False)

    assert renamed == [
        ("Screenshot 2026-03-01 at 12.00.00.png", "20260301_capture.png")
    ]

    # Verify file was actually renamed on disk and content is preserved
    assert not file1.exists()
    new_file = tmp_path / "20260301_capture.png"
    assert new_file.exists()
    assert new_file.read_text() == "dummy content 1"


def test_bulk_rename_no_matches(tmp_path):
    file1 = tmp_path / "document.pdf"
    file1.write_text("pdf content")

    pattern = r"Screenshot.*"
    replacement = r"new.png"

    renamed = bulk_rename(str(tmp_path), pattern, replacement, dry_run=True)

    assert renamed == []
    assert file1.exists()
