from django.shortcuts import render, redirect
from django.db import connection
from .sql_queries import *

def execute_sql(sql, params=None):
    with connection.cursor() as cursor:
        cursor.execute(sql, params or [])
        if cursor.description:
            return cursor.fetchall()
    return None

# Students
def student_list(request):
    students = execute_sql(GET_STUDENTS_LIST)
    return render(request, 'students/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        class_id = request.POST.get('class_id') or None
        execute_sql(INSERT_STUDENT, [first_name, last_name, class_id])
        return redirect('student_list')

    classes = execute_sql(GET_CLASSES)
    return render(request, 'students/add_student.html', {'classes': classes})

def update_student(request, id):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        class_id = request.POST.get('class_id') or None
        execute_sql(UPDATE_STUDENT, [first_name, last_name, class_id, id])
        return redirect('student_list')

    student = execute_sql(GET_STUDENT_BY_ID, [id])[0]
    classes = execute_sql(GET_CLASSES)
    return render(request, 'students/update_student.html', {'student': student, 'classes': classes})

def delete_student(request, id):
    execute_sql(DELETE_STUDENT, [id])
    return redirect('student_list')

# Grades
def grade_list(request):
    grades = execute_sql(GET_GRADES_LIST)
    return render(request, 'students/grade_list.html', {'grades': grades})

def add_grade(request):
    if request.method == 'POST':
        grade = request.POST['grade']
        date = request.POST['date']
        student_id = request.POST['student_id']
        subject_id = request.POST['subject_id']
        execute_sql(INSERT_GRADE, [grade, date, student_id, subject_id])
        return redirect('grade_list')

    students = execute_sql(GET_STUDENTS)
    subjects = execute_sql(GET_SUBJECTS)
    return render(request, 'students/add_grade.html', {'students': students, 'subjects': subjects})

def update_grade(request, id):
    if request.method == 'POST':
        grade = request.POST['grade']
        date = request.POST['date']
        student_id = request.POST['student_id']
        subject_id = request.POST['subject_id']
        execute_sql(UPDATE_GRADE, [grade, date, student_id, subject_id, id])
        return redirect('grade_list')

    grade = execute_sql(GET_GRADE_BY_ID, [id])[0]
    students = execute_sql(GET_STUDENTS)
    subjects = execute_sql(GET_SUBJECTS)
    return render(request, 'students/update_grade.html', {'grade': grade, 'students': students, 'subjects': subjects})

def delete_grade(request, id):
    execute_sql(DELETE_GRADE, [id])
    return redirect('grade_list')
