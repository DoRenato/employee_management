from django.db import models

# Create your models here.


class Department(models.Model):
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.department


class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    birth_date = models.DateField()

    def __str__(self):
        return self.name