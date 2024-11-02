from django.db import models
from django.core.exceptions import ValidationError


class Reservation(models.Model):
    """
    A printer reservation.
    """

    owner = models.CharField(
        max_length=255, help_text="The name of the person doing the reservation"
    )
    start = models.DateTimeField(help_text="When the reservation starts")
    end = models.DateTimeField(help_text="When the reservation ends")

    def clean(self):
        conflicts = Reservation.objects.exclude(pk=self.pk).filter(
            start__lt=self.end, end__gt=self.start
        )
        if conflicts.exists():
            raise ValidationError("Conflicting reservation by %s" % conflicts[0].owner)

    def __str__(self):
        return "%s from %s to %s" % (self.owner, self.start, self.end)

    class Meta:
        ordering = ("start",)
