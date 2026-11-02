import random
import requests


from urls import BASE_URL


def generate_email():
    return f"user_{random.randint(100000, 999999)}@ya.ru"


def generate_password():
    return str(random.randint(100000, 999999999))


def register_user():
    email = generate_email()
    password = generate_password()

    payload = {
        "email": email,
        "password": password,
        "name": "TestUser"
    }

    response = requests.post(
        f"{BASE_URL}/api/auth/register",
        json=payload
    )

    access_token = response.json()["accessToken"]

    return email, password, access_token


def delete_user(access_token):
    requests.delete(
        f"{BASE_URL}/api/auth/user",
        headers={
            "Authorization": access_token
        }
    )