from django.shortcuts import render, redirect, get_object_or_404
from . import sql_queries
from django.db import connection

def fetch_all(query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params or [])
        return cursor.fetchall()

def execute_query(query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params or [])

def schedule_list(request):
    schedules = fetch_all(sql_queries.GET_ALL_SCHEDULES)
    return render(request, 'schedule/schedule_list.html', {'schedules': schedules})

def add_schedule(request):
    if request.method == 'POST':
        weekday = request.POST['weekday']
        lesson_number = request.POST['lesson_number']
        cabinet_id = request.POST.get('cabinet_id') or None
        class_id = request.POST.get('class_id') or None
        teacher_id = request.POST.get('teacher_id') or None

        try:
            execute_query(sql_queries.ADD_SCHEDULE, [weekday, lesson_number, cabinet_id, class_id, teacher_id])
            return redirect('schedule_list')
        except Exception as e:
            print(f"Error adding schedule: {e}")

    cabinets = fetch_all(sql_queries.GET_ALL_CABINETS)
    classes = fetch_all(sql_queries.GET_ALL_CLASSES)
    teachers = fetch_all(sql_queries.GET_ALL_TEACHERS)

    return render(request, 'schedule/add_schedule.html', {
        'cabinets': cabinets,
        'classes': classes,
        'teachers': teachers,
    })


def update_schedule(request, schedule_id):
    schedule = fetch_all(sql_queries.GET_SCHEDULE_BY_ID, [schedule_id])[0]
    if request.method == 'POST':
        weekday = request.POST['weekday']
        lesson_number = request.POST['lesson_number']
        cabinet_id = request.POST.get('cabinet_id') or None
        class_id = request.POST.get('class_id') or None
        teacher_id = request.POST.get('teacher_id') or None

        execute_query(sql_queries.UPDATE_SCHEDULE, [weekday, lesson_number, cabinet_id, class_id, teacher_id, schedule_id])
        return redirect('schedule_list')

    cabinets = fetch_all(sql_queries.GET_ALL_CABINETS)
    classes = fetch_all(sql_queries.GET_ALL_CLASSES)
    teachers = fetch_all(sql_queries.GET_ALL_TEACHERS)
    return render(request, 'schedule/update_schedule.html', {
        'schedule': schedule,
        'cabinets': cabinets,
        'classes': classes,
        'teachers': teachers,
    })


def delete_schedule(request, schedule_id):
    execute_query(sql_queries.DELETE_SCHEDULE, [schedule_id])
    return redirect('schedule_list')
