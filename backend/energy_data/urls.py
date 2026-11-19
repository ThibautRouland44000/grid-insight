from django.urls import path

from .views import ReadingListView, health

urlpatterns = [
    path("health/", health),
    path("readings/", ReadingListView.as_view(), name="reading-List"),
]
