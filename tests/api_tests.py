import os

from pytest_voluptuous import S
from schemas.users import user, users, create_user
from utils.sessions import session


def test_list_users_validation():
    page = 2
    response = session().get("/users", params={"page": page})

    assert response.status_code == 200
    assert S(users) == response.json()


def test_single_user_validation():
    response = session().get("/users/2")

    assert S(user) == response.json()


def test_create_user_validation():
    name = "morph"
    job = "qa"
    user_data = {"name": name, "job": job}
    response = session().post("/users", json=user_data)

    assert response.status_code == 201
    assert S(create_user) == response.json()


def test_delete_user():
    response = session().delete("/users/2")

    assert response.status_code == 204


def test_register_user():
    EMAIL = os.getenv('email')
    PASSWORD = os.getenv('password')
    user_credentials = {"email": EMAIL, "password": PASSWORD}
    response = session().post("/register", json=user_credentials)

    assert response.status_code == 200
    assert len(response.json()["token"]) == 17
