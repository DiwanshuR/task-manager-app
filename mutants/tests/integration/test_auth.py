from datetime import datetime


def register_user(client, email="alex@example.com"):
    return client.post(
        "/auth/register",
        json={
            "name": "Alex",
            "email": email,
            "password": "TestPassword123!",
        },
    )


def test_register_user(client):
    response = register_user(client)

    assert response.status_code == 201
    assert response.json()["email"] == "alex@example.com"
    assert datetime.fromisoformat(
        response.json()["created_at"]
    ).utcoffset() is not None


def test_register_rejects_duplicate_email(client):
    first_response = register_user(client)
    second_response = register_user(client)

    assert first_response.status_code == 201
    assert second_response.status_code == 409


def test_login_returns_tokens(client):
    register_user(client)

    response = client.post(
        "/auth/login",
        data={
            # OAuth2PasswordRequestForm expects the field to be named "username",
            # even though your app uses the value as an email address.
            "username": "alex@example.com",
            "password": "TestPassword123!",
        },
    )

    assert response.status_code == 200
    assert response.json()["access_token"]
    assert response.json()["refresh_token"]
    assert response.json()["token_type"] == "bearer"


def test_login_rejects_wrong_password(client):
    register_user(client)

    response = client.post(
        "/auth/login",
        data={
            "username": "alex@example.com",
            "password": "WrongPassword123!",
        },
    )

    assert response.status_code == 401

# 4. Test the user-enumeration case: assert the login error body for "unknown user" is byte-identical to "wrong password".
def test_login_error_body_is_identical_for_unknown_user_and_wrong_password(
    client,
):
    register_user(client)

    wrong_password = client.post(
        "/auth/login",
        data={
            "username": "alex@example.com",
            "password": "WrongPassword123!",
        },
    )
    unknown_user = client.post(
        "/auth/login",
        data={
            "username": "unknown@example.com",
            "password": "WrongPassword123!",
        },
    )

    assert wrong_password.status_code == unknown_user.status_code == 401
    assert wrong_password.content == unknown_user.content