from django import forms

class ScheduleQueryForm(forms.Form):
    class_id = forms.IntegerField(label="Класс", required=False)
    weekday = forms.ChoiceField(
        label="День недели", 
        choices=[
            ("Monday", "Понедельник"), 
            ("Tuesday", "Вторник"), 
            ("Wednesday", "Среда"), 
            ("Thursday", "Четверг"), 
            ("Friday", "Пятница")
        ],
        required=False
    )
    lesson_number = forms.IntegerField(label="Номер урока", required=False)
    teacher_id = forms.IntegerField(label="Учитель", required=False)
    subject_id = forms.IntegerField(label="Предмет", required=False)

class StatisticsForm(forms.Form):
    class_id = forms.IntegerField(label="Класс", required=False)
    include_grades_distribution = forms.BooleanField(
        label="Включить распределение оценок", required=False
    )
