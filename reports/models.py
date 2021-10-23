from django.db import models

# Modelo para armazenar o menor e maior salário, assim como a média dos dois
class ReportSalary(models.Model):
    lowest = models.TextField()
    highest = models.TextField()
    average = models.CharField(max_length=7)

    def __str__(self):
        return self.average


# Modelo para armazenar o funcionário mais novo e mais velhor, assim como a média entre de suas idades
class ReportAge(models.Model):
    younger = models.TextField()
    older = models.TextField()
    average = models.CharField(max_length=5)

    def __str__(self):
        return self.average