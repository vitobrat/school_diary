GET_ALL_SCHEDULES = """
SELECT s.id, s.weekday, s.lesson_number, 
       c.number AS cabinet, cl.name AS class, 
       t.full_name AS teacher, sub.name AS subject
FROM schedule s
LEFT JOIN cabinets c ON s.cabinet_id = c.id
LEFT JOIN classes cl ON s.class_id = cl.id
LEFT JOIN teachers t ON s.teacher_id = t.id
LEFT JOIN subjects sub ON t.subject_id = sub.id
ORDER BY s.weekday, s.lesson_number;
"""


GET_SCHEDULE_BY_ID = """
SELECT id, weekday, lesson_number, cabinet_id, class_id, teacher_id
FROM schedule
WHERE id = %s;
"""


ADD_SCHEDULE = """
INSERT INTO schedule (weekday, lesson_number, cabinet_id, class_id, teacher_id)
VALUES (%s, %s, %s, %s, %s);
"""


UPDATE_SCHEDULE = """
UPDATE schedule
SET weekday = %s, lesson_number = %s, cabinet_id = %s, class_id = %s, teacher_id = %s
WHERE id = %s;
"""


DELETE_SCHEDULE = """
DELETE FROM schedule
WHERE id = %s;
"""


GET_ALL_CABINETS = "SELECT id, number FROM cabinets;"


GET_ALL_CLASSES = "SELECT id, name FROM classes;"


GET_ALL_TEACHERS = "SELECT id, full_name FROM teachers;"


GET_ALL_SUBJECTS = "SELECT id, name FROM subjects;"
