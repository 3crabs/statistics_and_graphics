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

    def get_done_coef(self):
        if self.count_done and self.count_views:
            return self.count_done / self.count_views
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
            return self.count_views / self.count_in
        return "-"

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
            return str(datetime.datetime.fromtimestamp(self.last_access))
        return "-"
