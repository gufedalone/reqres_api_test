import requests
from pytest_voluptuous import S

from schemas.users import user, users, create_user


def test_list_users_validation():
    page = 2
    response = requests.get("https://reqres.in/api/users", params={"page": page})

    assert response.status_code == 200
    assert S(users) == response.json()


def test_single_user_validation():
    response = requests.get("https://reqres.in/api/users/2")

    assert S(user) == response.json()


def test_create_user_validation():
    name = "morph"
    job = "qa"
    user_data = {"name": name, "job": job}
    response = requests.post("https://reqres.in/api/users", json=user_data)

    assert response.status_code == 201
    assert S(create_user) == response.json()


def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2")

    assert response.status_code == 204


def test_register_user():
    email = "eve.holt@reqres.in"
    password = "pistol"
    user_credentials = {"email": email, "password": password}
    response = requests.post("https://reqres.in/api/register", json=user_credentials)

    assert response.status_code == 200
    assert len(response.json()["token"]) == 17
