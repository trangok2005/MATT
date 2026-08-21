def test_login_success(client):
    response = client.post(
        "/",
        data={
            "email": "trang@ok",
            "pswd": "123"
        }
    )
    assert response.status_code == 405


def test_login_fail(client):
    response = client.post(
        "/",
        data={
            "email": "abc",
            "pswd": "111"
        }
    )
    assert response.status_code == 405

