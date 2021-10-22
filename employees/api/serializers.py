from rest_framework.serializers import ModelSerializer
from employees.models import *


class EmployeesSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','name','email','department','salary','birth_date')