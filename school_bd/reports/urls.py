from django.urls import path
from . import views

urlpatterns = [
    path("schedule_queries/", views.schedule_queries, name="schedule_queries"),
    path("statistics/", views.statistics, name="statistics"),
]
