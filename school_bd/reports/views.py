from django.shortcuts import render
from django.db import connection
from .forms import ScheduleQueryForm, StatisticsForm
from .sql_queries import *

def schedule_queries(request):
    results = None
    form = ScheduleQueryForm(request.GET or None)
    if form.is_valid():
        # Здесь вызывается соответствующий SQL-запрос
        # и возвращаются данные.
        class_id = form.cleaned_data["class_id"]
        weekday = form.cleaned_data["weekday"]
        lesson_number = form.cleaned_data["lesson_number"]
        teacher_id = form.cleaned_data["teacher_id"]
        subject_id = form.cleaned_data["subject_id"]
        
        with connection.cursor() as cursor:
            # Использовать подходящий SQL-запрос
            cursor.execute(GET_SCHEDULE_FOR_CLASS, [class_id, weekday, lesson_number, teacher_id, subject_id])
            results = cursor.fetchall()

    return render(request, "reports/schedule_queries.html", {"form": form, "results": results})

def statistics(request):
    results = None
    form = StatisticsForm(request.GET or None)
    if form.is_valid():
        class_id = form.cleaned_data["class_id"]
        include_grades_distribution = form.cleaned_data["include_grades_distribution"]

        with connection.cursor() as cursor:
            cursor.execute(GET_OVERALL_STATISTICS, [class_id])
            results = cursor.fetchall()

    return render(request, "reports/statistics.html", {"form": form, "results": results})
