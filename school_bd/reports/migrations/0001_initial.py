from django.db import migrations

def create_reports_table(apps, schema_editor):
    with open('reports/sql/create_reports_table.sql', 'r') as f:
        sql = f.read()
    schema_editor.execute(sql)

def drop_reports_table(apps, schema_editor):
    schema_editor.execute('DROP TABLE IF EXISTS reports')

class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.RunPython(create_reports_table, reverse_code=drop_reports_table),
    ]