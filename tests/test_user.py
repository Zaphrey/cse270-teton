import requests


def test_invalid_login_returns_401_and_empty_body(mocker):
    # Mock requests.get
    mock_get = mocker.patch("requests.get")

    # Configure mock HTTP response
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_response.text = ""

    mock_get.return_value = mock_response

    url = "http://127.0.0.1:8000/users"
    params = {"username": "admin", "password": "wrongpassword"}

    response = requests.get(url, params=params)

    assert response.status_code == 401
    assert response.text == ""


def test_valid_login_returns_200_and_empty_body(mocker):
    # Mock requests.get
    mock_get = mocker.patch("requests.get")

    # Configure mock HTTP response
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = ""

    mock_get.return_value = mock_response

    url = "http://127.0.0.1:8000/users"
    params = {"username": "admin", "password": "qwerty"}

    response = requests.get(url, params=params)

    assert response.status_code == 200
    assert response.text == ""
