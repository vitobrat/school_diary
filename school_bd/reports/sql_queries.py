GET_CLASSES = """
    SELECT id, name
    FROM classes
"""

GET_TEACHERS = """
    SELECT id, full_name
    FROM teachers
"""

GET_SUBJECTS = """
    SELECT id, name
    FROM subjects
"""

GET_SUBJECT_BY_FILTER = """
    SELECT DISTINCT subjects.name
    FROM schedule
    LEFT JOIN teachers ON schedule.teacher_id = teachers.id
    LEFT JOIN subjects ON teachers.subject_id = subjects.id
    LEFT JOIN classes ON schedule.class_id = classes.id
    WHERE schedule.weekday = %s AND schedule.class_id = %s AND schedule.lesson_number = %s
"""

GET_TEACHERS_BY_FILTER = """
    SELECT DISTINCT teachers.full_name
    FROM schedule
    LEFT JOIN teachers ON schedule.teacher_id = teachers.id
    LEFT JOIN classes ON schedule.class_id = classes.id
    WHERE schedule.class_id = %s
"""

GET_CABINET_BY_FILTER = """
    SELECT DISTINCT cabinets.number
    FROM schedule
    LEFT JOIN cabinets ON schedule.cabinet_id = cabinets.id
    LEFT JOIN classes ON schedule.class_id = classes.id
    WHERE schedule.lesson_number = %s AND schedule.weekday = %s AND schedule.class_id = %s
"""

GET_CLASSES_BY_FILTER = """
    SELECT DISTINCT classes.name
    FROM schedule
    LEFT JOIN teachers ON schedule.teacher_id = teachers.id
    LEFT JOIN classes ON schedule.class_id = classes.id
    LEFT JOIN subjects ON teachers.subject_id = subjects.id
    WHERE schedule.teacher_id = %s
"""

GET_SCHEDULE_BY_FILTER = """
    SELECT DISTINCT schedule.weekday, schedule.lesson_number, cabinets.number, classes.name, teachers.full_name, subjects.name
    FROM schedule
    LEFT JOIN teachers ON schedule.teacher_id = teachers.id
    LEFT JOIN classes ON schedule.class_id = classes.id
    LEFT JOIN subjects ON teachers.subject_id = subjects.id
    LEFT JOIN cabinets ON schedule.cabinet_id = cabinets.id
    WHERE schedule.weekday = %s AND schedule.class_id = %s
    ORDER BY schedule.lesson_number
"""

COUNT_STUDENT_IN_CLASS = """
    SELECT COUNT(students.id)
    FROM students
    LEFT JOIN classes ON students.class_id = classes.id
    WHERE students.class_id = %s
"""

COUNT_TEACHERS_BY_SUBJECT = """
    SELECT subjects.name, COUNT(teachers.full_name)
    FROM teachers
    LEFT JOIN subjects ON teachers.subject_id = subjects.id
    GROUP BY subjects.name
"""

COUNT_CABINETS = """
    SELECT COUNT(id)
    FROM cabinets
"""

COUNT_STUDENTS_IN_EACH_CLASS = """
    SELECT classes.name, COUNT(students.id)
    FROM students
    LEFT JOIN classes ON students.class_id = classes.id
    GROUP BY classes.name
"""

COUNT_2_GRADES_BY_CLASS = """
    SELECT classes.name, COUNT(grades.id)
    FROM grades
    LEFT JOIN students ON grades.student_id = students.id
    LEFT JOIN classes ON students.class_id = classes.id
    WHERE grades.grade = 2
    GROUP BY classes.name
"""

COUNT_4_GRADES_BY_CLASS = """
    SELECT classes.name, COUNT(grades.id)
    FROM grades
    LEFT JOIN students ON grades.student_id = students.id
    LEFT JOIN classes ON students.class_id = classes.id
    WHERE grades.grade = 4
    GROUP BY classes.name
"""

COUNT_5_GRADES_BY_CLASS = """
    SELECT classes.name, COUNT(grades.id)
    FROM grades
    LEFT JOIN students ON grades.student_id = students.id
    LEFT JOIN classes ON students.class_id = classes.id
    WHERE grades.grade = 5
    GROUP BY classes.name
"""
