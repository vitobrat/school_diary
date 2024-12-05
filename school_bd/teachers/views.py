from django.shortcuts import render, redirect
from django.db import connection
from .sql_queries import *

def execute_sql(sql, params=None):
    with connection.cursor() as cursor:
        cursor.execute(sql, params or [])
        if cursor.description:  # Если запрос возвращает данные
            return cursor.fetchall()
    return None

def teacher_list(request):
    teachers = execute_sql(GET_TEACHERS_LIST)
    return render(request, 'teachers/teacher_list.html', {'teachers': teachers})

def add_teacher(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        subject_id = request.POST['subject_id']
        cabinet_id = request.POST.get('cabinet_id') or None
        execute_sql(INSERT_TEACHER, [full_name, subject_id, cabinet_id])
        return redirect('teacher_list')

    subjects = execute_sql(GET_SUBJECTS)
    cabinets = execute_sql(GET_CABINETS)
    return render(request, 'teachers/add_teacher.html', {'subjects': subjects, 'cabinets': cabinets})

def delete_teacher(request, id):
    execute_sql(DELETE_TEACHER, [id])
    return redirect('teacher_list')

def update_teacher(request, id):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        subject_id = request.POST['subject_id']
        cabinet_id = request.POST.get('cabinet_id') or None
        execute_sql(UPDATE_TEACHER, [full_name, subject_id, cabinet_id, id])
        return redirect('teacher_list')

    teacher = execute_sql(GET_TEACHER_BY_ID, [id])[0]
    subjects = execute_sql(GET_SUBJECTS)
    cabinets = execute_sql(GET_CABINETS)
    return render(request, 'teachers/update_teacher.html', {'teacher': teacher, 'subjects': subjects, 'cabinets': cabinets})
