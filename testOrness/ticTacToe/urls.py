from django.urls import path

from .views import Advertisements

urlpatterns = [
    path("x/", Advertisements.as_view(), name="x"),
    path("o/", Advertisements.as_view(), name="o"),
]