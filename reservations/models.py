from django.db import models
from django.core.exceptions import ValidationError


class Reservation(models.Model):
    """
    A printer reservation.
    """

    PRINTER_PRUSA = "prusaxl"
    PRINTER_ULTIMAKER = "ultimaker2+"
    PRINTER_ELEGOO_MARS = "elegoo-mars"
    PRINTER_ELEGOO_SATURN4ULTRA = "elegoo-saturn-4ultra"
    PRINTER_CHOICES = {
        PRINTER_PRUSA: "Prusa XL",
        PRINTER_ULTIMAKER: "Ultimaker 2+",
        PRINTER_ELEGOO_MARS: "Elegoo Mars",
        PRINTER_ELEGOO_SATURN4ULTRA: "Elegoo Saturn 4 Ultra",
    }

    owner = models.CharField(
        max_length=255, help_text="The name of the person doing the reservation"
    )
    printer = models.CharField(
        max_length=255,
        help_text="The printer for which a reservation should be added",
        choices=[
            (PRINTER_PRUSA, PRINTER_CHOICES[PRINTER_PRUSA]),
            (PRINTER_ULTIMAKER, PRINTER_CHOICES[PRINTER_ULTIMAKER]),
            (PRINTER_ELEGOO_MARS, PRINTER_CHOICES[PRINTER_ELEGOO_MARS]),
            (PRINTER_ELEGOO_SATURN4ULTRA, PRINTER_CHOICES[PRINTER_ELEGOO_SATURN4ULTRA]),
        ],
    )
    start = models.DateTimeField(help_text="When the reservation starts")
    end = models.DateTimeField(help_text="When the reservation ends")

    def clean(self):
        super().clean()

        # Detect conflicts
        if self.start is not None and self.end is not None:
            conflicts = Reservation.objects.exclude(pk=self.pk).filter(
                printer=self.printer, start__lt=self.end, end__gt=self.start
            )
            if conflicts.exists():
                raise ValidationError("Conflicting reservation by %s" % conflicts[0].owner)

    def __str__(self):
        return (
            f"{self.owner} ({self.PRINTER_CHOICES[self.printer]}) from {self.start} to {self.end}"
        )

    class Meta:
        ordering = ("start",)
