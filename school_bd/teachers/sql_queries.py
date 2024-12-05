GET_TEACHERS_LIST = """
    SELECT t.id, t.full_name, s.name AS subject, c.number AS cabinet
    FROM teachers t
    LEFT JOIN subjects s ON t.subject_id = s.id
    LEFT JOIN cabinets c ON t.cabinet_id = c.id
"""

INSERT_TEACHER = """
    INSERT INTO teachers (full_name, subject_id, cabinet_id) VALUES (%s, %s, %s)
"""

DELETE_TEACHER = """
    DELETE FROM teachers WHERE id = %s
"""

UPDATE_TEACHER = """
    UPDATE teachers
    SET full_name = %s, subject_id = %s, cabinet_id = %s
    WHERE id = %s
"""

GET_SUBJECTS = "SELECT id, name FROM subjects"
GET_CABINETS = "SELECT id, number FROM cabinets"

GET_TEACHER_BY_ID = """
    SELECT id, full_name, subject_id, cabinet_id FROM teachers WHERE id = %s
"""
