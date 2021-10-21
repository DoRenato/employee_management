from rest_framework.fields import ModelField, SerializerMethodField
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from employees.models import *


class EmployeesSerializer(ModelSerializer):
    department = SerializerMethodField()
    class Meta:
        model = Employee
        fields = ('id','name','email','department','salary','birth_date')
    
    def get_department(self, obj):
        return "%s" %(obj.department) # Poderia ser tambem: return "{}".format(obj.department) 