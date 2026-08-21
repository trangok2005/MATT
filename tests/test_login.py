def test_login_success(client):
    response = client.post(
        "/",
        data={
            "email": "trang@ok",
            "pswd": "123"
        }
    )
    assert response.status_code == 200


def test_login_fail(client):
    response = client.post(
        "/",
        data={
            "email": "abc",
            "pswd": "111"
        }
    )
    assert response.status_code == 200
from dao import login

def test_login_valid_credentials():
    assert login("trang@ok", "123") == True

def test_login_invalid_username():
    assert login("sai", "123") == False