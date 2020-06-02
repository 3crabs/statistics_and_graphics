import datetime

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    last_access = models.IntegerField()
    end_grade_id = models.IntegerField()
    end_grade = models.IntegerField()
    end_grade_max = models.IntegerField()
    count_course = models.IntegerField()
    courses = []
    count_in = models.IntegerField()
    count_views = models.IntegerField()
    count_done = models.IntegerField()
    count_all = models.IntegerField()
    final_grade = models.IntegerField()

    def get_done_coef(self):
        if self.count_done and self.count_views:
            return int(self.count_done * 100 / self.count_views) / 100
        return 0

    def get_count_done(self):
        if self.count_done and self.count_all:
            return str(self.count_done) + '/' + str(self.count_all)
        return 0

    def get_count_in(self):
        if self.count_in:
            return self.count_in
        return 0

    def get_count_views(self):
        if self.count_views:
            return self.count_views
        return 0

    def get_coef(self):
        if self.count_in and self.count_views:
            return int(self.count_views * 100 / self.count_in) / 100
        return "-"

    def get_end_grade(self):
        if self.end_grade:
            return int(self.end_grade * 100) / 100
        return "-"

    def get_end_grade_max(self):
        if self.end_grade_max:
            return int(self.end_grade_max * 100) / 100
        return "-"

    def get_last_access(self):
        if self.last_access:
            return str(datetime.datetime.fromtimestamp(self.last_access))
        return "-"

    def get_final_grade(self):
        if self.final_grade:
            return int(self.final_grade * 100) / 100
        return '-'
