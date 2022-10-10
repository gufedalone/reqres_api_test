import os
from utils.requests_helpers import BaseSession


def reqres() -> BaseSession:
    reqres_url = os.getenv("base_url")
    return BaseSession(base_url=reqres_url)
