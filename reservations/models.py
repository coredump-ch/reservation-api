from django.db import models


class Reservation(models.Model):
    """
    A printer reservation.
    """
    owner = models.CharField(max_length=255,
            help_text='The name of the person doing the reservation')
    start = models.DateTimeField(help_text='When the reservation starts')
    end = models.DateTimeField(help_text='When the reservation ends')

    def __str__(self):
        return '%s from %s to %s' % (self.owner, self.start, self.end)

    class Meta:
        ordering = ('start',)
