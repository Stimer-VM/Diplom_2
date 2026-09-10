import requests

from data import INVALID_INGREDIENT_ORDER, VALID_INGREDIENTS, ERROR_INGREDIENT_IDS, ERROR_INVALID_INGREDIENT
from urls import BASE_URL, CREATE_ORDER


class TestCreateOrder:
    def test_create_order_with_authorization(self, auth_user):
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

    def test_create_order_without_authorization(self):
        response = requests.post(
            BASE_URL + CREATE_ORDER,
            json={
                "ingredients": VALID_INGREDIENTS
            }
        )

        assert response.status_code == 200
        assert response.json()["success"] is True

    def test_create_order_without_ingredients(self, auth_user):
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
        assert response.json()["message"] == ERROR_INGREDIENT_IDS

    def test_create_order_with_invalid_ingredient(self, auth_user):
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
        assert response.json()["message"] == ERROR_INVALID_INGREDIENT