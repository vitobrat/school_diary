from django.shortcuts import render
from django.db import connection
from .sql_queries import *

def execute_sql(sql, params=None):
    with connection.cursor() as cursor:
        cursor.execute(sql, params or [])
        if cursor.description:
            return cursor.fetchall()
    return None


def schedule_queries(request):
    results = {}
    if request.method == 'POST':
        class_id = request.POST.get("class_id")
        weekday = request.POST.get("weekday")
        lesson_number = request.POST.get("lesson_number")
        teacher_id = request.POST.get("teacher_id")
        subject_id = request.POST.get("subject_id")
        print(class_id, weekday, lesson_number, teacher_id, subject_id)
        if weekday and class_id and lesson_number:
            results["subject"] = execute_sql(GET_SUBJECT_BY_FILTER, [weekday, class_id, lesson_number])
        if class_id:
            results["teachers"] = execute_sql(GET_TEACHERS_BY_FILTER, [class_id])
        if weekday and lesson_number and class_id:
            results["cabinet"] = execute_sql(GET_CABINET_BY_FILTER, [lesson_number, weekday, class_id])
        if teacher_id:
            results["classes"] = execute_sql(GET_CLASSES_BY_FILTER, [teacher_id])
        if weekday and class_id:
            results["schedule"] = execute_sql(GET_SCHEDULE_BY_FILTER, [weekday, class_id])

    subjects = execute_sql(GET_SUBJECTS)
    classes = execute_sql(GET_CLASSES)
    teachers = execute_sql(GET_TEACHERS)
    print(results)

    return render(
        request,
        "reports/schedule_queries.html",
        {
            "subjects": subjects,
            "classes": classes,
            "results": results,
            "teachers": teachers,
        },
    )


def statistics(request):
    results = {}
    if request.method == 'POST':
        class_id = request.POST.get("class_id")

        if class_id:
            results["students_count"] = execute_sql(COUNT_STUDENT_IN_CLASS, [class_id])
        results["teachers_by_subject"] = execute_sql(COUNT_TEACHERS_BY_SUBJECT)
        results["cabinets_count"] = execute_sql(COUNT_CABINETS)
        results["students_by_class"] = execute_sql(COUNT_STUDENTS_IN_EACH_CLASS)
        results["grades_by_class"] = {
            "twos": execute_sql(COUNT_2_GRADES_BY_CLASS),
            "fours": execute_sql(COUNT_4_GRADES_BY_CLASS),
            "fives": execute_sql(COUNT_5_GRADES_BY_CLASS),
        }

    classes = execute_sql(GET_CLASSES)

    # Преобразование данных
    if results.get("teachers_by_subject"):
        results["teachers_by_subject"] = [
            {"subject": row[0], "count": row[1]} for row in results["teachers_by_subject"]
        ]
    if results.get("students_by_class"):
        results["students_by_class"] = [
            {"class_name": row[0], "count": row[1]} for row in results["students_by_class"]
        ]
    if results.get("grades_by_class"):
        for grade_type in ["twos", "fours", "fives"]:
            results["grades_by_class"][grade_type] = [
                {"class_name": row[0], "count": row[1]} for row in results["grades_by_class"][grade_type]
            ]

    return render(request, "reports/statistics.html", {"results": results, "classes": classes})

