import requests

from data import INVALID_INGREDIENT_ORDER, VALID_INGREDIENTS
from urls import BASE_URL, CREATE_ORDER


def test_create_order_with_authorization(auth_user):
    _, access_token = auth_user

    response = requests.post(
        BASE_URL + CREATE_ORDER,
        headers={
            "Authorization": access_token
        },
        json={
            "ingredients": VALID_INGREDIENTS
        }
    )

    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "order" in response.json()


def test_create_order_without_authorization():
    response = requests.post(
        BASE_URL + CREATE_ORDER,
        json={
            "ingredients": VALID_INGREDIENTS
        }
    )

    assert response.status_code == 200
    assert response.json()["success"] is True


def test_create_order_without_ingredients(auth_user):
    _, access_token = auth_user

    response = requests.post(
        BASE_URL + CREATE_ORDER,
        headers={
            "Authorization": access_token
        },
        json={
            "ingredients": []
        }
    )

    assert response.status_code == 400
    assert response.json()["success"] is False


def test_create_order_with_invalid_ingredient(auth_user):
    _, access_token = auth_user

    response = requests.post(
        BASE_URL + CREATE_ORDER,
        headers={
            "Authorization": access_token
        },
        json=INVALID_INGREDIENT_ORDER
    )

    assert response.status_code == 400
    assert response.json()["success"] is False