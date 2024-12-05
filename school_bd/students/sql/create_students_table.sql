CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    class_id INTEGER,
    CONSTRAINT fk_class FOREIGN KEY (class_id) REFERENCES classes(id) ON DELETE SET NULL
);