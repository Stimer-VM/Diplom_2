PASSWORD = "TestPassword123"
NAME = "Test User"

INVALID_PASSWORD = "WrongPassword123"

EMPTY_ORDER = {
    "ingredients": []
}

INVALID_INGREDIENT_ORDER = {
    "ingredients": ["invalid_hash"]
}

VALID_INGREDIENTS = [
    "61c0c5a71d1f82001bdaaa6d",
    "61c0c5a71d1f82001bdaaa6f"
]

ERROR_INGREDIENT_IDS = "Ingredient ids must be provided"
ERROR_USER_EXISTS = "User already exists"
ERROR_LOGIN_WRONG_PASSWORD = "email or password are incorrect"
ERROR_INVALID_INGREDIENT = "One or more ids provided are incorrect"