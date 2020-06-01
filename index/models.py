import datetime

from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    count_user = models.IntegerField()
    last_access = models.IntegerField()

    def get_last_access(self):
        if self.last_access:
            return datetime.datetime.fromtimestamp(self.last_access)
        return "-"


class GradeItems(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    grade_min = models.IntegerField()
    grade_max = models.IntegerField()
    grade = models.IntegerField()
    grade_id = models.IntegerField()

    def get_type(self):
        if self.type == 'quiz':
            return "Тест"
        elif self.type == 'assign':
            return "Задание"
        elif self.type == 'lesson':
            return "Лекция"
        else:
            return "-"

    def get_grade(self):
        if self.grade:
            return str(self.grade)
        return str(self.grade_min)
