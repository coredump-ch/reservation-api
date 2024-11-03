from datetime import timedelta

import pytest
from model_bakery import baker
from django.utils import timezone
from django.core.exceptions import ValidationError


# Useful times
now = timezone.now()
delta = timedelta(hours=1)

# Recipe Alias
UltimakerReservation = "reservations.UltimakerReservation"
PrusaReservation = "reservations.PrusaReservation"


@pytest.mark.parametrize(
    ["instance", "conflict"],
    [
        # Regular overlaps
        (
            baker.prepare_recipe(
                UltimakerReservation,
                start=now,
                end=now + delta * 2,
            ),
            True,
        ),
        (
            baker.prepare_recipe(
                UltimakerReservation,
                start=now - delta / 2,
                end=now + delta / 2,
            ),
            True,
        ),
        (
            baker.prepare_recipe(
                UltimakerReservation,
                start=now - delta * 2,
                end=now,
            ),
            True,
        ),
        # Start or end are equal
        (
            baker.prepare_recipe(
                UltimakerReservation,
                start=now - delta,
                end=now,
            ),
            True,
        ),
        (
            baker.prepare_recipe(
                UltimakerReservation,
                start=now,
                end=now + delta,
            ),
            True,
        ),
        (
            baker.prepare_recipe(
                UltimakerReservation,
                start=now - delta,
                end=now + delta,
            ),
            True,
        ),
        # Non conflicts
        (
            # Ends earlier
            baker.prepare_recipe(
                UltimakerReservation,
                start=now - delta * 3,
                end=now - delta * 2,
            ),
            False,
        ),
        (
            # Ends when current reservation starts
            baker.prepare_recipe(
                UltimakerReservation,
                start=now - delta * 2,
                end=now - delta,
            ),
            False,
        ),
        (
            # Starts when current reservation ends
            baker.prepare_recipe(
                UltimakerReservation,
                start=now + delta,
                end=now + delta * 2,
            ),
            False,
        ),
        (
            # Different printer
            baker.prepare_recipe(
                PrusaReservation,
                start=now,
                end=now + delta * 2,
            ),
            False,
        ),
    ],
)
@pytest.mark.django_db
def test_reservation_conflict(instance, conflict):
    res = baker.make_recipe(UltimakerReservation, start=now - delta, end=now + delta)
    res.full_clean()

    if conflict is True:
        with pytest.raises(ValidationError):
            instance.full_clean()
    else:
        instance.full_clean()
