from django.db import migrations

def create_teachers_tables(apps, schema_editor):
    with open('teachers/sql/create_subjects_table.sql', 'r') as f:
        schema_editor.execute(f.read())
    with open('teachers/sql/create_cabinets_table.sql', 'r') as f:
        schema_editor.execute(f.read())
    with open('teachers/sql/create_teachers_table.sql', 'r') as f:
        schema_editor.execute(f.read())

def drop_teachers_tables(apps, schema_editor):
    schema_editor.execute('DROP TABLE IF EXISTS teachers')
    schema_editor.execute('DROP TABLE IF EXISTS subjects')
    schema_editor.execute('DROP TABLE IF EXISTS cabinets')

class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.RunPython(create_teachers_tables, reverse_code=drop_teachers_tables),
    ]
