from rest_framework import serializers

from . import models


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Reservation
        fields = ('pk', 'owner', 'start', 'duration')
