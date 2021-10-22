from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import *
from employees.models import *


class EmployeesViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer

    # Sobrescrevendo a action POST
    def create(self, request, *args, **kwargs):
        data = request.data # Pego todos os dados enviados através da requisição POST e armazeno nesta variável.

        # O Django por padrão não aceita o formato da data em dd-mm-aaaa, portanto, decidi implementar o método a seguir para
        # receber o JSON exatamente da forma do exemplo (dd-mm-aaaa) e salvá-lo no banco com o formato válido (aaaa-mm-dd).
        birth = [x for x in data['birth_date'].split("-")] # pego a data que foi enviada no formato dd-mm-aaaa e transformo em uma lista [dd, mm, aaaa]
        birth.reverse() # inverto a ordem da lista, então agora está [aaaa, mm, dd]
        birth="{}-{}-{}".format(birth[0], birth[1], birth[2]) # apenas tiro do formato de lista em deixo em formato de string "aaaa-mm-dd", que é válido para salvar no modelo.
        # ======

        employee = Employee() # Criando um novo modelo do Tipo Funcionário, este modelo tem os mesmos campos do Exemplo do teste técnico.
        employee.name = data['name']
        employee.department = data['department']
        employee.salary = data['salary']
        employee.email = data['email']
        employee.birth_date = birth # Recebe a data que foi convertida no incio dessa action.
        employee.save()

        return Response("A new employee has been registered successfully.")

    # Action PUT
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # Action PATCH
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)