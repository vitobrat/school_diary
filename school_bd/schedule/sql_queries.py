# Получить все записи расписания
GET_ALL_SCHEDULES = """
SELECT s.id, s.weekday, s.lesson_number, 
       c.number AS cabinet, cl.name AS class, 
       t.full_name AS teacher, sub.name AS subject
FROM schedule s
LEFT JOIN cabinets c ON s.cabinet_id = c.id
LEFT JOIN classes cl ON s.class_id = cl.id
LEFT JOIN teachers t ON s.teacher_id = t.id
LEFT JOIN subjects sub ON s.subject_id = sub.id
ORDER BY s.weekday, s.lesson_number;
"""

# Получить одну запись расписания по ID
GET_SCHEDULE_BY_ID = """
SELECT id, weekday, lesson_number, cabinet_id, class_id, teacher_id, subject_id
FROM schedule
WHERE id = %s;
"""

# Добавить новую запись в расписание
ADD_SCHEDULE = """
INSERT INTO schedule (weekday, lesson_number, cabinet_id, class_id, teacher_id, subject_id)
VALUES (%s, %s, %s, %s, %s, %s);
"""

# Обновить запись расписания
UPDATE_SCHEDULE = """
UPDATE schedule
SET weekday = %s, lesson_number = %s, cabinet_id = %s, class_id = %s, teacher_id = %s, subject_id = %s
WHERE id = %s;
"""

# Удалить запись расписания
DELETE_SCHEDULE = """
DELETE FROM schedule
WHERE id = %s;
"""

# Получить все кабинеты
GET_ALL_CABINETS = "SELECT id, number FROM cabinets;"

# Получить все классы
GET_ALL_CLASSES = "SELECT id, name FROM classes;"

# Получить всех учителей
GET_ALL_TEACHERS = "SELECT id, full_name FROM teachers;"

# Получить все предметы
GET_ALL_SUBJECTS = "SELECT id, name FROM subjects;"
