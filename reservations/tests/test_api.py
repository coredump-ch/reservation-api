from datetime import timedelta

from django.utils import timezone
from model_bakery import baker
import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from reservations.models import Reservation


@pytest.mark.django_db
@pytest.fixture(scope="function")
def api_client():
    token = baker.make(Token)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
    return client


@pytest.mark.django_db
def test_create_success(api_client):
    """
    Successfully create reservation.
    """
    r = api_client.post(
        "/api/v1/reservations/",
        {
            "owner": "Test",
            "printer": "ultimaker2+",
            "start": "2017-04-02T22:05:00Z",
            "end": "2017-04-02T23:00:00Z",
        },
    )
    assert r.status_code == 201, r.data


@pytest.mark.django_db
def test_empty_duration(api_client):
    """
    Regression test for issue 3.
    """
    r1 = api_client.post(
        "/api/v1/reservations/",
        {
            "owner": "Test",
            "start": "2017-04-02T22:05:00Z",
            "end": "",
        },
    )
    r2 = api_client.post(
        "/api/v1/reservations/",
        {
            "owner": "Test",
            "start": "2017-04-02T22:05:00Z",
        },
    )
    assert r1.status_code == 400
    assert r2.status_code == 400


@pytest.mark.django_db
def test_pagination(api_client):
    """
    Ensure pagination is enabled
    """
    baker.make(
        Reservation,
        start=timezone.now(),
        end=timezone.now() + timedelta(hours=3),
        _quantity=30,
    )
    r1 = api_client.get("/api/v1/reservations/")
    assert set(r1.data.keys()) == {"results", "previous", "count", "next"}
    assert r1.data["count"] == 30  # Total available
    assert len(r1.data["results"]) == 20  # Returned per page
