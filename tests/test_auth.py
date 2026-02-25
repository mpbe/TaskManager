
def test_register_user_success(client):

    response = client.post("/auth/register", data={
        "username": "test",
        "email": "test@test.com",
        "password": "test"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Task List for" in response.data


def test_login_user_success(client):

    client.post("/auth/register", data={
        "username": "test",
        "email": "test@test.com",
        "password": "test"
    })

    response = client.post("/auth/login", data={
        "username": "test",
        "password": "test"
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Task List for" in response.data


def test_login_user_failure(client):

    response = client.post("/auth/login", data={
        "username": "fail",
        "password": "fail"
    }, follow_redirects=True)

    assert b"user not in database" in response.data


def test_register_invalid_email(client):

    response = client.post("/auth/register", data={
        "username": "correct",
        "email": "wrong",
        "password": "correct"
    }, follow_redirects=True)

    assert b"email is in incorrect format" in response.data


def test_register_duplicate_email(client):

    client.post("/auth/register", data={
        "username": "user a",
        "email": "duplicate@email.com",
        "password": "password"
    })

    response = client.post("/auth/register", data={
        "username": "user b",
        "email": "duplicate@email.com",
        "password": "password"
    }, follow_redirects=True)

    assert b"email already exists in database" in response.data


def test_register_duplicate_username(client):

    client.post("/auth/register", data={
        "username": "user a",
        "email": "test@email.com",
        "password": "password"
    })

    response = client.post("/auth/register", data={
        "username": "user a",
        "email": "test2@email.com",
        "password": "password"
    }, follow_redirects=True)

    assert b"user already exists in database" in response.data



# logout works