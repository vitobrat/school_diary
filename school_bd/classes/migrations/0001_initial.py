from django.db import migrations

def create_classes_table(apps, schema_editor):
    with open('classes/sql/create_classes_table.sql', 'r') as f:
        sql = f.read()
    schema_editor.execute(sql)

def drop_classes_table(apps, schema_editor):
    schema_editor.execute('DROP TABLE IF EXISTS classes')

class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.RunPython(create_classes_table, reverse_code=drop_classes_table),
    ]