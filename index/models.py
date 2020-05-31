from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    count_user = models.IntegerField()


class GradeItems(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    grade_min = models.IntegerField()
    grade_max = models.IntegerField()
    grade = models.IntegerField()

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
            return str(int(self.grade)) + '/' + str(int(self.grade_max))
        return str(int(self.grade_min)) + '/' + str(int(self.grade_max))
