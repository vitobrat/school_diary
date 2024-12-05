from django.db import migrations

def create_schedule_table(apps, schema_editor):
    with open('schedule/sql/create_schedule_table.sql', 'r') as f:
        sql = f.read()
    schema_editor.execute(sql)

def drop_schedule_table(apps, schema_editor):
    schema_editor.execute('DROP TABLE IF EXISTS schedule')

class Migration(migrations.Migration):
    dependencies = [
        ('classes', '0001_initial'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_schedule_table, reverse_code=drop_schedule_table),
    ]