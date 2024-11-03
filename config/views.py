from django.db import connection
from django.http import JsonResponse


def healthcheck(request):
    """
    Ensure that the application is healthy.
    """
    with connection.cursor() as cursor:
        cursor.execute("SELECT count(*) FROM django_migrations")
        count = cursor.fetchone()[0]
    if count > 0:
        return JsonResponse({"db": "ok"}, status=200)
    else:
        return JsonResponse({"db": "error, no migrations applied"}, status=500)
