# Ultimaker Reservation API

A small Python 3 / Django 1.8 project to manage reservations for our 3D printer.


## API Endpoints

- `GET /api/v1/reservations/` - List reservations
- `POST /api/v1/reservations/` - Create new reservation
- `GET /api/v1/reservations/<id>/` - Show reservation details
- `PUT /api/v1/reservations/<id>/` - Update reservation
- `PATCH /api/v1/reservations/<id>/` - Update reservation
- `DELETE /api/v1/reservations/<id>/` - Delete reservation


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

## License

AGPLv3 License.
