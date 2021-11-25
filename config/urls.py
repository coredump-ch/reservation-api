from django.urls import include, re_path
from django.contrib import admin

from reservations import urls as reservation_urls

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/v1/', include(reservation_urls)),
]
