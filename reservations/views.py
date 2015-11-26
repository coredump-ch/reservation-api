from rest_framework import viewsets

from . import serializers, models


class ReservationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reservations to be viewed or edited.
    """
    queryset = models.Reservation.objects.all()
    serializer_class = serializers.ReservationSerializer
