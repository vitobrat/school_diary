from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_list, name='schedule_list'),
    path('add/', views.add_schedule, name='add_schedule'),
    path('update/<int:schedule_id>/', views.update_schedule, name='update_schedule'),
    path('delete/<int:schedule_id>/', views.delete_schedule, name='delete_schedule'),
]
