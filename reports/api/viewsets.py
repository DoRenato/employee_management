from django.db.models import Min, Max
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from datetime import date

from employees.api.serializers import EmployeesSerializer
from .serializers import *

from employees.models import *
from reports.models import *

def convert2Json(queryset): #Função para converter todos os dados que estão no formato queryset em um dicionário python.
    dictionary={}
    dictionary['id'] = str(queryset.id) # Como o ID é um campo do tipo Inteiro(int) no queryset, converto ele para string(str).
    dictionary['name'] = queryset.name
    dictionary['email'] = queryset.email
    dictionary['department'] = queryset.department
    dictionary['salary'] = str(queryset.salary) # Situação semelhante do ID, mas neste campo o formato é do tipo DecimalField(Ou float).
    dictionary['birth_date'] = queryset.birth_date.strftime('%d-%m-%Y') # Apanas modificando a data padrão de 'aaaa-mm-dd' para 'dd-mm-aaaa' através da função 'strftime()'
    return dictionary

def calculate_age(born): # Função para calcular a idade atual
    today = date.today() # através da biblioteca 'date' do python, posso pegar o data atual do sistema chamando a função 'today()'.
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day)) # Diminui primeiro o ano de nascimento do ano atual, e então faz a subtração dos meses/dias.


class ReportSalaryViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [IsAuthenticated, ] # Define qual o tipo permissão será aceita, neste caso, será permitido acessar essa ViewSet se o usuario estiver autenticado.
    authentication_classes = [TokenAuthentication, ] # Define qual o tipo de autenticação é utilizada, neste caso utilizei autenticação por Token, que considero mais eficaz.

    
    ## Sobrescrevendo a Action GET
    def list(self, request, *args, **kwargs):

        ## PEGANDO O MENOR SALÁRIO ===
        lowest = self.queryset.aggregate(Min('salary')) # Busca em todos os funcionários cadastrados quais tem o menor valor de salário.
        lowest = Employee.objects.filter(salary = lowest['salary__min']) # Filtra e retorna uma lista com todos os dados de todos os funcionários que tiveram o menor valor encontrado. 
        lowest = lowest[0] # Como todos os encontrados tem o mesmo salário, então basta pegar somente o primeiro da lista.
        lowest = convert2Json(lowest) # Converte a lista do tipo <QueryDict> em formato de JSON

        ## PEGANDO O MAIOR SALÁRIO ===
        highest = self.queryset.aggregate(Max('salary')) # Busca em todos os funcionários cadastrados quais tem o maior valor de salário.
        highest = Employee.objects.filter(salary = highest['salary__max']) # Filtra e retorna uma lista com todos os dados de todos os funcionários que tiveram o maior valor encontrado. 
        highest = highest[0] # Como todos os encontrados tem o mesmo salário, então basta pegar somente o primeiro da lista.
        highest = convert2Json(highest)
        
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

        dictionary={}
        dictionary['lowest'] = salary.lowest
        dictionary['highest'] = salary.highest
        dictionary['average'] =  salary.average

        return Response (dictionary)


"""
Para o EndPoint de verificação das idades, a lógica foi quase que igual a do Salário (ViewSet acima), só mudou o nome das variáveis
bem dizer, portanto, só irei comentar as alterações mais específicas deste Endpoint.
"""
class ReportAgeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeesSerializer
    permission_classes = [IsAuthenticated, ] # Define qual o tipo permissão será aceita, neste caso, será permitido acessar essa ViewSet se o usuario estiver autenticado.
    authentication_classes = [TokenAuthentication, ] # Define qual o tipo de autenticação é utilizada, neste caso utilizei autenticação por Token, que considero mais eficaz.


    def list(self, request, *args, **kwargs):
        age_older = self.queryset.aggregate(Min('birth_date')) # Como no salário, mas ao invés de buscar o menor salário, busco a menor data do sistema.
        older = Employee.objects.filter(birth_date = age_older['birth_date__min'])
        older = older[0]
        older = convert2Json(older)

        age_younger = self.queryset.aggregate(Max('birth_date'))
        younger = Employee.objects.filter(birth_date = age_younger['birth_date__max'])
        younger = younger[0]
        younger = convert2Json(younger)
        
        average = (calculate_age(age_older['birth_date__min']) + calculate_age(age_younger['birth_date__max']))/2
        average="{:.2f}".format(average)

        age = ReportAge.objects.all() 
        if len(age) == 0: 
            age = ReportAge() 
        else:
            age = ReportAge.objects.get(id=age[0].id)
        age.younger = younger
        age.older = older
        age.average = average
        age.save()

        dictionary={}
        dictionary['younger']=age.younger
        dictionary['older']=age.older
        dictionary['average']=age.average
        
        return Response(dictionary)