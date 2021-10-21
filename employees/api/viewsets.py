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

        # Como não consegui fazer com que o django aceite o formato da data em dd/mm/aaaa enquanto a localização estiver en-us,
        # decidi fazer este método para conseguir receber o JSON exatamente da forma do exemplo (dd/mm/aaaa) e salvá-lo no banco com
        # o formato válido.
        date = [x for x in data['birth_date'].split("-")] # pego a data que foi enviada no formato dd/mm/aaaa e transformo em uma lista [dd, mm, aaaa]
        date.reverse() # inverto a lista, então agora está [aaaa, mm, dd]
        date="{}-{}-{}".format(date[0], date[1], date[2]) # apenas tiro do formato de lista em deixo em formato de string: dd-mm-aaaa
        # ======
        
        # Decidi criar um modelo separado para os departamentos, então cada departamento será salvo no banco, assim, quando novos
        # funcionários forem cadastrados, o departamento será uma chave estrangeira:
        try:
            department = Department.objects.get(department = data["department"]) #| busca no banco se existe algum departamento com o nome igual ao do novo funcionario a ser cadastrado,
                                                                                 #| se o departamento já existir, então será armazenado nesta variavel para ser atribuido ao novo funcionário.
        except:
            department = Department() # Se não existir ainda o departamento do novo funcionário, então será criado no banco.
            department.department = data["department"]
            department.save()

        employee = Employee() # Criando um novo modelo do Tipo Funcionário, este modelo tem os mesmos campos do Exemplo.
        employee.name = data['name']
        employee.department = department # Ao invés de receber o nome do departamento, vai receber o departamento de mesmo nome que já esta cadastrado no banco.
        employee.salary = data['salary']
        employee.email = data['email']
        employee.birth_date = date # Recebe a data que foi convertida no incio dessa action.
        employee.save()

        return Response("A new employee has been registered successfully.")

    # Como o departamento é uma Chave estrangeira, precisei sobrescrever as duas actions a seguir para poder atualizar esta chave
    # sempre que necessário.
    
    # Sobrescrevendo a action PUT
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            department = Department.objects.get(department = request.data["department"])
        except:
            department = Department()
            department.department = request.data["department"]
            department.save()

        employee = Employee.objects.get(id=instance.id)
        employee.department = department
        employee.save()
        return Response('PUT sucessfully.')
    
    # Sobrescrevendo a action PATCH
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            department = Department.objects.get(department = request.data["department"])
        except:
            department = Department()
            department.department = request.data["department"]
            department.save()
        employee = Employee.objects.get(id=instance.id)
        employee.department = department
        employee.save()
        return Response('PATCH sucessfully.')