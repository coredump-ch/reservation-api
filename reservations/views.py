from django.utils import timezone

from rest_framework import viewsets

from . import serializers, models


class ReservationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reservations to be viewed or edited.
    """

    serializer_class = serializers.ReservationSerializer

    def get_queryset(self):
        """
        Return filtered or non-filtered queryset, depending on GET parameters.
        """
        history = self.request.query_params.get("includeHistory", "").lower() in [
            "true",
            "1",
            "yes",
            "y",
        ]
        if self.action == "list" and not history:
            return models.Reservation.objects.filter(end__gte=timezone.now())
        else:
            return models.Reservation.objects.all()
