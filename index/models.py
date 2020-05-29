from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    count_user = models.IntegerField()
    avg = models.IntegerField()
    last_time = models.IntegerField()
    count_entry = models.IntegerField()
    count_viewed = models.IntegerField()
    count_modules = models.IntegerField()
