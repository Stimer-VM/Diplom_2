import requests

from data import ERROR_LOGIN_WRONG_PASSWORD
from urls import BASE_URL, LOGIN_USER


class TestLogin:
    def test_login_existing_user(self, created_user):
        user_data, registration_response = created_user

        assert registration_response.status_code == 200
        assert registration_response.json()["success"] is True

        response = requests.post(
            BASE_URL + LOGIN_USER,
            json={
                "email": user_data["email"],
                "password": user_data["password"]
            }
        )

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()

    def test_login_with_wrong_password(self, created_user):
        user_data, registration_response = created_user

        assert registration_response.status_code == 200

        response = requests.post(
            BASE_URL + LOGIN_USER,
            json={
                "email": user_data["email"],
                "password": "WrongPassword123"
            }
        )

        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == ERROR_LOGIN_WRONG_PASSWORD