# Students
GET_STUDENTS_LIST = """
    SELECT s.id, s.first_name, s.last_name, c.name AS class_name
    FROM students s
    LEFT JOIN classes c ON s.class_id = c.id
"""

INSERT_STUDENT = """
    INSERT INTO students (first_name, last_name, class_id) VALUES (%s, %s, %s)
"""

UPDATE_STUDENT = """
    UPDATE students
    SET first_name = %s, last_name = %s, class_id = %s
    WHERE id = %s
"""

DELETE_STUDENT = """
    DELETE FROM students WHERE id = %s
"""

GET_STUDENT_BY_ID = """
    SELECT id, first_name, last_name, class_id FROM students WHERE id = %s
"""

GET_CLASSES = "SELECT id, name FROM classes"

# Grades
GET_GRADES_LIST = """
    SELECT g.id, g.grade, g.date, s.first_name || ' ' || s.last_name AS student_name, 
           subj.name AS subject_name
    FROM grades g
    LEFT JOIN students s ON g.student_id = s.id
    LEFT JOIN subjects subj ON g.subject_id = subj.id
"""

INSERT_GRADE = """
    INSERT INTO grades (grade, date, student_id, subject_id) VALUES (%s, %s, %s, %s)
"""

UPDATE_GRADE = """
    UPDATE grades
    SET grade = %s, date = %s, student_id = %s, subject_id = %s
    WHERE id = %s
"""

DELETE_GRADE = """
    DELETE FROM grades WHERE id = %s
"""

GET_GRADE_BY_ID = """
    SELECT id, grade, date, student_id, subject_id FROM grades WHERE id = %s
"""

GET_SUBJECTS = "SELECT id, name FROM subjects"
GET_STUDENTS = "SELECT id, first_name || ' ' || last_name AS name FROM students"
