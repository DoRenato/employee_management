from rest_framework.viewsets import ModelViewSet
from .serializers import *
from employees.models import *


class EmployeesViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)