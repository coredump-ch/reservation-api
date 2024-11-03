from rest_framework import serializers

from . import models


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    def validate(self, attrs):
        instance = models.Reservation(**attrs)
        instance.clean()
        return attrs

    class Meta:
        model = models.Reservation
        fields = ("pk", "url", "owner", "printer", "start", "end")
