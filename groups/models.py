from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)
    count_users = models.IntegerField()
    academic_performance = models.IntegerField()

    def get_academic_performance(self):
        if self.academic_performance:
            return int(self.academic_performance * 100) / 100
