# Sobre a API:

## Importante

### Observação
Para cadastrar um novo funcionário não é necessário incluir o campo ID, pois o framework gera automaticamente este campo.

### API no Ar

A API está hospedada no Heroku, portanto, caso queira testar o funcionamento por completo antes de instalar na própria máquina, segue os Endpoints: 
- https://emp-man-sw.herokuapp.com/employees/ - gerenciamento dos funcionários (GET, POST)
- https://emp-man-sw.herokuapp.com/employees/ID/ - gerenciamento de um funcionário específico (DETALHE, UPDATE, DELETE)
- https://emp-man-sw.herokuapp.com/reports/employees/salary/ - Relatório de salário
- https://emp-man-sw.herokuapp.com/reports/employees/age/ - Relatório de Idade

    * Para fazer todas as requisições utilizei o Postman.
    * Todos os Endpoints precisam de autenticação, mais abaixo explico como autenticar para acessà-los.
    * Sim, o **sw** no final do host é de Star Wars haha

## Requisitos e Execução

Para contrução desta API utilizei o **Django Rest Framework**, um framework para desenvolvimentos de API's Rest de código aberto todo escrito na linguagem de programação **Python**. A seguir irei explicar como funciona e o que será necessário para executar a aplicação:

- É recomendável configurar um ambiente virtual para instalar os requisitos, todos os necessários estão no arquivo **requirements-dev.txt**
    * O python tem seu proprio ambiente virtual, para instalar o comando é *python -m venv nome_do_seu_ambiente*
    * Se for Windows, para ativa-lo vá para pasta de ativação *nome_do_seu_ambiente/Scripts/* e execute o comando *./activate*
    * Com o ambiente ativado, basta instalar os requisitos pelo **pip**, por padrao o comando é *pip install nome_requisito*
- Com os requisitos instalados, vá para pasta raiz do projeto pelo terminal e execute o comando *python manage.py migrate* para criar o banco de dados no sistema.
    * A pasta raiz do projeto é a que contem o arquivo **manage.py**
- Rode o servidor local através do comando *python manage.py runserver* (que pode ser acessado através do link http://localhost:8000/)

E Pronto, tudo está preparado e funcionando para execução da API.

## Autenticação

- Cadastre um novo usuario no sistema: http://localhost:8000/users/register
- Utilizando o Postman ou qualquer outro API client, faça uma requição POST em http://localhost:8000/api-token-auth/ para receber o **Token** de Autorização necessário para acessar os Endpoints. O conteúdo da requisição deve ser o seguinte JSON:  
```
{
    "username": "user_que_foi_cadastrado",
    "password": "senha_do_user_cadastrado"
}
```
- Com o **Token** gerado, é preciso adicioná-lo ao Header sempre que for fazer qualquer requisição em qualquer Endpoint da API. A imagem a seguir mostra como dever ser adicionado utilizando o Postman:

![Autenticação](https://raw.githubusercontent.com/DoRenato/employee_management/master/token.png)

Com isso, o acesso a API está liberado para fazer qualquer uma das operações esperadas.

### Extras
- O código está todo comentando, busquei explicar cada passo do algorítmo para melhor entendimento da lógica.
- Caso queira acessar o banco para verificar todos os dados armazenados, os passos são:
1. Vá para pasta raiz do projeto e através do terminal execute o comando *python manage.py createsuperuser* e coloque as credenciais requisitadas.
2. Com o super usuário criado, acesse http://localhost:8000/admin/ e faça login. Com isso, você terá acesso a todas os dados cadastrados no banco.

- Tanto os Endpoints do servidor local quanto do Heroku são os mesmos, só muda os hosts.