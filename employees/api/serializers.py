from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from employees.models import *


class EmployeesSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','name','email','department','salary','birth_date')