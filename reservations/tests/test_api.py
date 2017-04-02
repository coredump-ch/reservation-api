import pytest
from rest_framework.test import APIClient
from model_mommy import mommy
from rest_framework.authtoken.models import Token


@pytest.mark.django_db
@pytest.fixture(scope='function')
def api_client():
    token = mommy.make(Token)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return client


@pytest.mark.django_db
def test_empty_duration(api_client):
    """
    Regression test for issue 3.
    """
    r1 = api_client.post('/api/v1/reservations/', {
        'owner': 'Test',
        'start': '2017-04-02T22:05:00Z',
        'end': '',
    })
    r2 = api_client.post('/api/v1/reservations/', {
        'owner': 'Test',
        'start': '2017-04-02T22:05:00Z',
    })
    assert r1.status_code == 400
    assert r2.status_code == 400
