from django.urls import path

from .views import PlayX, Play0

urlpatterns = [
    path("x/", PlayX.as_view(), name="play-x"),
    path("o/", Play0.as_view(), name="play-o"),
]