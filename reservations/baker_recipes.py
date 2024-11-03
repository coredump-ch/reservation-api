from model_bakery.recipe import Recipe
from .models import Reservation

UltimakerReservation = Recipe(Reservation, printer=Reservation.PRINTER_ULTIMAKER)
PrusaReservation = Recipe(Reservation, printer=Reservation.PRINTER_PRUSA)
