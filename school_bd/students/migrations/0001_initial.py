from django.db import migrations

def create_students_table(apps, schema_editor):
     with open('students/sql/create_students_table.sql', 'r') as f:
        schema_editor.execute(f.read())
     with open('students/sql/create_grades_table.sql', 'r') as f:
        schema_editor.execute(f.read())
    

def drop_students_table(apps, schema_editor):
    schema_editor.execute('DROP TABLE IF EXISTS students')
    schema_editor.execute('DROP TABLE IF EXISTS grades')

class Migration(migrations.Migration):
    dependencies = [
        ('classes', '0001_initial'),
        ('teachers', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_students_table, reverse_code=drop_students_table),
    ]