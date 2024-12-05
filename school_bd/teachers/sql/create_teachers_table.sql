CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    subject_id INTEGER NOT NULL,
    cabinet_id INTEGER,
    CONSTRAINT fk_subject FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE,
    CONSTRAINT fk_cabinet FOREIGN KEY (cabinet_id) REFERENCES cabinets(id) ON DELETE SET NULL
);
