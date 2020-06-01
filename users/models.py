import datetime

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    last_access = models.IntegerField()
    end_grade_id = models.IntegerField()
    end_grade = models.IntegerField()
    end_grade_max = models.IntegerField()
    count_course = models.IntegerField()

    def get_end_grade(self):
        if self.end_grade:
            return self.end_grade
        return "-"

    def get_end_grade_max(self):
        if self.end_grade_max:
            return self.end_grade_max
        return "-"

    def get_last_access(self):
        if self.last_access:
            return datetime.datetime.fromtimestamp(self.last_access)
        return "-"
