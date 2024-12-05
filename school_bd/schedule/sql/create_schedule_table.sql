CREATE TABLE schedule (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    weekday TEXT NOT NULL,
    lesson_number INTEGER NOT NULL,
    cabinet_id INTEGER,
    class_id INTEGER,
    teacher_id INTEGER,
    subject_id INTEGER,
    CONSTRAINT fk_cabinet FOREIGN KEY (cabinet_id) REFERENCES cabinets(id) ON DELETE SET NULL,
    CONSTRAINT fk_class FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE SET NULL,
    CONSTRAINT fk_teacher FOREIGN KEY (teacher_id) REFERENCES teachers(id) ON DELETE SET NULL,
    CONSTRAINT fk_subject FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE SET NULL
);
