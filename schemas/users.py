from voluptuous import ALLOW_EXTRA
from voluptuous import Schema

user = Schema(
    {
        "data": {
            "id": int,
            "email": str,
            "first_name": str,
            "last_name": str,
            "avatar": str
        }
    }, extra=ALLOW_EXTRA)

users = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": [user]
    }, extra=ALLOW_EXTRA)

create_user = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    })
