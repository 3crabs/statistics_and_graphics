import datetime

from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    count_user = models.IntegerField()


class User(models.Model):
    name = models.CharField(max_length=100)
    last_access = models.IntegerField()

    def get_last_access(self):
        return datetime.datetime.fromtimestamp(self.last_access)


class GradeItems(models.Model):
    name = models.CharField(max_length=100)
    last_access = models.IntegerField()
