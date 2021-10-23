from rest_framework.serializers import ModelSerializer
from employees.models import *

# Classe onde irá serializar os dados.
class EmployeesSerializer(ModelSerializer):
    class Meta:
        model = Employee # Busca o modelo no banco que será serializado
        fields = ('id','name','email','department','salary','birth_date') # Aqui defino quais campos deste modelo eu quero que apareçam na serialização