import datetime

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    last_access = models.IntegerField()
    end_grade = models.IntegerField()

    def get_last_access(self):
        if self.last_access:
            return datetime.datetime.fromtimestamp(self.last_access)
        return "-"
