
def test_register_user_success(client):

    response = client.post("/auth/register", data={
        "username": "test",
        "email": "test@test.com",
        "password": "test"
    })
    assert response.status_code == 302


def test_login_user_success(client):

    client.post("auth/register", data={
        "username": "test",
        "email": "test@test.com",
        "password": "test"
    })

    response = client.post("auth/login", data={
        "username": "test",
        "password": "password"
    })

    assert response.status_code == 302