from datetime import timedelta

import pytest
from model_bakery import baker
from django.utils import timezone
from django.core.exceptions import ValidationError

from reservations import models


# Useful times
now = timezone.now()
delta = timedelta(hours=1)


@pytest.mark.parametrize(
    ["instance", "conflict"],
    [
        # Regular overlaps
        (baker.prepare(models.Reservation, start=now, end=now + delta * 2), True),
        (
            baker.prepare(
                models.Reservation, start=now - delta / 2, end=now + delta / 2
            ),
            True,
        ),
        (baker.prepare(models.Reservation, start=now - delta * 2, end=now), True),
        # Start or end are equal
        (baker.prepare(models.Reservation, start=now - delta, end=now), True),
        (baker.prepare(models.Reservation, start=now, end=now + delta), True),
        (baker.prepare(models.Reservation, start=now - delta, end=now + delta), True),
        # Non conflicts
        (
            baker.prepare(
                models.Reservation, start=now - delta * 3, end=now - delta * 2
            ),
            False,
        ),
        (
            baker.prepare(models.Reservation, start=now - delta * 2, end=now - delta),
            False,
        ),
        (
            baker.prepare(models.Reservation, start=now + delta, end=now + delta * 2),
            False,
        ),
    ],
)
@pytest.mark.django_db
def test_reservation_conflict(instance, conflict):
    res = baker.make(models.Reservation, start=now - delta, end=now + delta)
    res.full_clean()

    if conflict is True:
        with pytest.raises(ValidationError):
            instance.full_clean()
    else:
        instance.full_clean()
