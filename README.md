# Sobre a API:

## API no Ar

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
- Utilizando o Postman ou qualquer outro API client, faça uma requição POST em http://localhost:8000/api-token-auth/ enviando o seguinte JSON:  
```
{
    "username": user_que_foi_cadastrado,
    "password": senha_do_user_cadastrado
}
```
E a API irá retornar o **Token** de Autorização.






(ou https://emp-man-sw.herokuapp.com/users/register pelo heroku)