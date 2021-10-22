from django.db.models import Min, Max
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from datetime import datetime, date

from employees.api.serializers import EmployeesSerializer
from .serializers import *

from employees.models import *
from reports.models import *

def convertJson(queryset):
    data={}
    data['id'] = str(queryset.id)
    data['name'] = queryset.name
    data['email'] = queryset.email
    data['department'] = queryset.department
    data['salary'] = str(queryset.salary)
    data['birth_date'] = queryset.birth_date.strftime('%d-%m-%Y') 
    return data
    

class ReportSalaryViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer
    
    ## Sobrescrevendo a Action GET
    def list(self, request, *args, **kwargs):
        data={}

        ## PEGANDO O MENOR SALÁRIO ===
        lowest = self.queryset.aggregate(Min('salary')) # Busca em todos os funcionários cadastrados quais tem o menor valor de salário.
        lowest = Employee.objects.filter(salary = lowest['salary__min']) # Filtra e retorna uma lista com todos os dados de todos os funcionários que tiveram o menor valor encontrado. 
        lowest = lowest[0] # Como todos os encontrados tem o mesmo salário, então basta pegar somente o primeiro da lista.
        lowest = convertJson(lowest) # Converte a lista do tipo <QueryDict> em formato de JSON

        ## PEGANDO O MAIOR SALÁRIO ===
        highest = self.queryset.aggregate(Max('salary')) # Busca em todos os funcionários cadastrados quais tem o maior valor de salário.
        highest = Employee.objects.filter(salary = highest['salary__max']) # Filtra e retorna uma lista com todos os dados de todos os funcionários que tiveram o maior valor encontrado. 
        highest = highest[0] # Como todos os encontrados tem o mesmo salário, então basta pegar somente o primeiro da lista.
        highest = convertJson(highest)
        
        ## CALCULANDO A MÉDIA
        average = (float(lowest['salary']) + float(highest['salary']))/2 # Calcula a média entre os dois salários.
        average = "{:.2f}".format(average) # codigo apenas para o valor ser armazenado com duas casas decimais.

        """
        Agora com todos os dados corretos, a seguir irei armazená-los para futuras consultas no banco em si. O padrão que defini é que
        sempre terá apenas uma tabela do tipo Relatório de funcionário, assim sempre que algum valor for modificado nos cálculos, o mesmo
        irá substituir os valores da tabela existente.
        """
        salary = ReportSalary.objects.all() # buscando no banco "todos os modelos" do tipo Relatório de Salário
        if len(salary) == 0: # Condição para verificar se ainda não existe algum modelo cadastrado.
            salary = ReportSalary() # Caso não exista, cria um novo modelo.
        else:
            salary = ReportSalary.objects.get(id=salary[0].id) # Caso exista, vai instancia-lo para edição.
        salary.lowest = lowest
        salary.highest = highest
        salary.average = average
        salary.save()

        data['lowest'] = salary.lowest
        data['highest'] = salary.highest
        data['average'] =  salary.average

        return Response (data)


class ReportAgeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer