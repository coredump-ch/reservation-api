# Ultimaker Reservation API

[![Build Status](https://github.com/coredump-ch/reservation-api/workflows/CI/badge.svg)](https://github.com/coredump-ch/reservation-api/actions?query=branch%3Amain)

A small Python 3 / Django 4.2 LTS project to manage reservations for our 3D printer.

## API Tokens

You need an API token to be able to read or write from this API. Request one
from `danilo@coredump.ch`.

The token should be included in the `Authorization` HTTP header. The key should
be prefixed by the string literal "Token", with whitespace separating the two
strings. For example:

    Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

## API Endpoints

All endpoints are below `/api/v1`.

- `GET /reservations/` - List reservations
- `POST /reservations/` - Create new reservation
- `GET /reservations/<id>/` - Show reservation details
- `PUT /reservations/<id>/` - Update reservation
- `PATCH /reservations/<id>/` - Update reservation
- `DELETE /reservations/<id>/` - Delete reservation

Example: Create reservation.

    $ curl -H "Authorization: Token <token>" \
           -d "owner=Danilo&start=2020-10-12T15:00:00Z&end=2020-10-12T16:30:00Z" \
           /api/v1/reservations/

Output:

    {
        "pk": 3,
        "url": "http://localhost:8000/api/v1/reservations/3/",
        "owner": "Danilo",
        "start": "2020-10-12T15:00:00Z",
        "end": "2020-10-12T16:30:00Z"
    }

Example: Get paginated list of reservations.

    $ curl -H "Authorization: Token <token>" \
           /api/v1/reservations/

Output:

    {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "pk": 1,
                "url": "http://localhost:8000/api/v1/reservations/1/",
                "owner": "Danilo",
                "start": "2015-10-12T15:00:00Z",
                "end": "2015-10-12T16:30:00Z"
            },
            {
                "pk": 2,
                "url": "http://localhost:8000/api/v1/reservations/2/",
                "owner": "Danilo",
                "start": "2020-10-12T15:00:00Z",
                "end": "2020-10-13T15:00:00Z"
            }
        ]
    }

If there are multiple pages, you will find the corresponding URLs in the `next`
or `previous` response fields.

## Dev Setup: Docker Compose

Run `docker-compose up` and enjoy the dev server at `http://localhost:8000/`.

To run tests:

    docker compose exec web pytest

## Dev Setup: Manual

Prerequisites:

- Python 3.6+
- Pip
- PostgreSQL

Database:

    createdb reservations

Dependencies:

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements-dev.txt

Env vars:

    export DJANGO_DEBUG=True
    export PORT=8000
    export DATABASE_URL='postgres://localhost/reservations'

Migrate database:

    ./manage.py migrate

Run dev server:

    ./manage.py runserver

Run tests:

    pytest

## License

AGPLv3 License.
