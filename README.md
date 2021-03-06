# Ultimaker Reservation API

A small Python 3 / Django 1.11 LTS project to manage reservations for our 3D printer.


## API Tokens

You need an API token to be able to read or write from this API. Request one
from `danilo@coredump.ch`.

The token should be included in the `Authorization` HTTP header. e key should
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


## Dev Setup

Prerequisites:

- Python 3.3+
- Pip
- Virtualenvwrapper
- PostgreSQL

Database:

    createdb reservations

Dependencies:

    mkvirtualenv reservations
    pip install -r requirements.txt

Env vars:

    POSTACTIVATE=$VIRTUAL_ENV/$VIRTUALENVWRAPPER_ENV_BIN_DIR/postactivate
    echo "export DJANGO_DEBUG=True" >> $POSTACTIVATE
    echo "export PORT=8000" >> $POSTACTIVATE
    echo "export DATABASE_URL='postgres://localhost/reservations'" >> $POSTACTIVATE
    source $POSTACTIVATE

Migrate database:

    ./manage.py migrate

Run dev server:

    ./manage.py runserver

## Running the tests

Install dependencies:

    pip install -r requirements-dev.txt

Run tests:

    py.test

## License

AGPLv3 License.
