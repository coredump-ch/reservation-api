from django.db import models


class Reservation(models.Model):
    """
    A printer reservation.
    """
    owner = models.CharField(max_length=255,
            help_text='The name of the person doing the reservation')
    start = models.DateTimeField(help_text='When the reservation starts')
    duration = models.DurationField(help_text='How long the reservation lasts')

    def __str__(self):
        return '%s on %s for %s' % (self.owner, self.start, self.duration)
