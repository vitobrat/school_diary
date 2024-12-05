from django.urls import path
from . import views

urlpatterns = [
    # Students
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('update/<int:id>/', views.update_student, name='update_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),

    # Grades
    path('grades/', views.grade_list, name='grade_list'),
    path('grades/add/', views.add_grade, name='add_grade'),
    path('grades/update/<int:id>/', views.update_grade, name='update_grade'),
    path('grades/delete/<int:id>/', views.delete_grade, name='delete_grade'),
]
