from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from .serializers import *
from employees.models import *


class EmployeesViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [IsAuthenticated, ] # Define qual o tipo permissão será aceita, neste caso, será permitido acessar essa ViewSet se o usuario estiver autenticado.
    authentication_classes = [TokenAuthentication, ] # Define qual o tipo de autenticação é utilizada, neste caso utilizei autenticação por Token, que considero mais eficaz.


    # Sobrescrevendo a action POST
    def create(self, request, *args, **kwargs):
        dictionary = request.data # Pego todos os dados enviados através da requisição POST e armazeno nesta variável.

        # O Django por padrão não aceita o formato da data em dd-mm-aaaa, portanto, decidi implementar o método a seguir para
        # receber o JSON exatamente da forma do exemplo (dd-mm-aaaa) e salvá-lo no banco com o formato válido (aaaa-mm-dd).
        birth = [x for x in dictionary['birth_date'].split("-")] # pego a data que foi enviada no formato dd-mm-aaaa e transformo em uma lista [dd, mm, aaaa]
        birth.reverse() # inverto a ordem da lista, então agora está [aaaa, mm, dd]
        birth="{}-{}-{}".format(birth[0], birth[1], birth[2]) # apenas tiro do formato de lista em deixo em formato de string "aaaa-mm-dd", que é válido para salvar no modelo.
        # ======

        employee = Employee() # Criando um novo modelo do Tipo Funcionário, este modelo tem os mesmos campos do Exemplo do teste técnico.
        employee.name = dictionary['name'] # Preencho o campo 'name' do meu modelo com o 'name' que foi recebido pelo POST. A lógica é igual para as linhas abaixo.
        employee.department = dictionary['department']
        employee.salary = dictionary['salary']
        employee.email = dictionary['email']
        employee.birth_date = birth # Recebe a data que foi convertida no incio dessa action.
        employee.save() # Com tudo preenchido, o modelo é de fato salvo no banco assim criando uma nova tupla.

        return Response("A new employee has been registered successfully.")

    # Action PUT
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # Action PATCH
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)