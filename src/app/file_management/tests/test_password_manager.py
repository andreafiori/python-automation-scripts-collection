from security.password_manager import PasswordManager


def test_password_manager_encrypted_file_round_trip(tmp_path):
    key_path = tmp_path / "password.key"
    password_path = tmp_path / "passwords.txt"

    writer = PasswordManager()
    writer.create_key(key_path)
    writer.create_pwd_file(
        password_path,
        init_values={"example.com": "correct horse battery staple"},
    )
    writer.add_password("second.example", "another secret")

    assert "correct horse battery staple" not in password_path.read_text()
    assert "another secret" not in password_path.read_text()

    reader = PasswordManager()
    reader.load_key(key_path)
    reader.load_pwd_file(password_path)

    assert reader.get_password("example.com") == "correct horse battery staple"
    assert reader.get_password("second.example") == "another secret"
    assert reader.get_sites() == ["example.com", "second.example"]