import random
import string

import pytest
import requests

from urls import BASE_URL, REGISTER_USER, LOGIN_USER


def generate_email():
    random_string = ''.join(
        random.choices(string.ascii_lowercase + string.digits, k=10)
    )
    return f"test_{random_string}@example.com"


@pytest.fixture
def user_data():
    return {
        "email": generate_email(),
        "password": "TestPassword123",
        "name": "Test User"
    }


@pytest.fixture
def created_user(user_data):
    response = requests.post(
        BASE_URL + REGISTER_USER,
        json=user_data
    )

    yield user_data, response


@pytest.fixture
def auth_user(user_data):
    registration_response = requests.post(
        BASE_URL + REGISTER_USER,
        json=user_data
    )

    assert registration_response.status_code == 200

    login_response = requests.post(
        BASE_URL + LOGIN_USER,
        json={
            "email": user_data["email"],
            "password": user_data["password"]
        }
    )

    assert login_response.status_code == 200

    access_token = login_response.json()["accessToken"]

    yield user_data, access_token