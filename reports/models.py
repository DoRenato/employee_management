from django.db import models

# Create your models here.

class ReportSalary(models.Model):
    lowest = models.TextField()
    highest = models.TextField()
    average = models.CharField(max_length=7)

    def __str__(self):
        return self.average


class ReportAge(models.Model):
    younger = models.TextField()
    older = models.TextField()
    average = models.CharField(max_length=5)

    def __str__(self):
        return self.average