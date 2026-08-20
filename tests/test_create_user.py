import pytest
import requests

from urls import BASE_URL, REGISTER_USER


def test_create_unique_user(user_data):
    response = requests.post(
        BASE_URL + REGISTER_USER,
        json=user_data
    )

    assert response.status_code == 200
    assert response.json()["success"] is True


def test_create_existing_user(user_data):
    requests.post(
        BASE_URL + REGISTER_USER,
        json=user_data
    )

    response = requests.post(
        BASE_URL + REGISTER_USER,
        json=user_data
    )

    assert response.status_code == 403
    assert response.json()["success"] is False


@pytest.mark.parametrize("field", ["email", "password", "name"])
def test_create_user_without_required_field(user_data, field):
    user_data.pop(field)

    response = requests.post(
        BASE_URL + REGISTER_USER,
        json=user_data
    )

    assert response.status_code == 403
    assert response.json()["success"] is False