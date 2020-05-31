from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    count_user = models.IntegerField()


class User(models.Model):
    name = models.CharField(max_length=100)
