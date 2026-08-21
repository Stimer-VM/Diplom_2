import pytest
import requests

from data import ERROR_USER_EXISTS
from urls import BASE_URL, REGISTER_USER


class TestCreateUser:
    def test_create_unique_user(self, user_data):
        response = requests.post(
            BASE_URL + REGISTER_USER,
            json=user_data
        )

        assert response.status_code == 200
        assert response.json()["success"] is True

    def test_create_existing_user(self, user_data):
        requests.post(BASE_URL + REGISTER_USER, json=user_data)
        response = requests.post(BASE_URL + REGISTER_USER, json=user_data)

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == ERROR_USER_EXISTS

    @pytest.mark.parametrize("field", ["email", "password", "name"])
    def test_create_user_without_required_field(self, user_data, field):
        user_data.pop(field)

        response = requests.post(
            BASE_URL + REGISTER_USER,
            json=user_data
        )

        assert response.status_code == 403
        assert response.json()["success"] is False