from app.auth.security import hash_password, verify_password


def test_hash_password_does_not_return_plaintext():
    password = "TestPassword123!"

    password_hash = hash_password(password)

    assert password_hash != password


def test_verify_password_accepts_the_correct_password():
    password = "TestPassword123!"
    password_hash = hash_password(password)

    assert verify_password(password, password_hash) is True


def test_verify_password_rejects_the_wrong_password():
    password_hash = hash_password("TestPassword123!")

    assert verify_password("WrongPassword123!", password_hash) is False