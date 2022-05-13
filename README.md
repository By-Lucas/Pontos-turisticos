# Pontos turisticos

## Informações sobre o django

### Instalar as bibliotedas utilizadas

**Instalar as bibliotecas e criar ambiente virtual para prossegir**
*Instalar virtualenv para criar ambiente virtual*
~~~ shell
pip install virtualenv
~~~
*Criar ambiente virtual*
~~~ shell
python -m venv venv
~~~
*Ativar ambiente virtual*
~~~ shell
venv/scripts/activate
~~~
*Instalar as bibliotecas*
~~~ shell
pip install -r requirements.txt
~~~
#

## Abaixo é os comandos básicos e mais utilizados do django

**Criar um app Django**
~~~ shell
django-admin startproject NOME_DO_PROJETO
~~~
- Ao criar um projeto ele vai criar diversas pastas automaticamente


**Criar um app no django**
~~~ shell
python manage.py startapp NOME_DO_APP
~~~
- Apos criar um app voce vai  no settings do app criado e identifica o INSTALLEDA_PPS = ['NOME_DO_APP'] E ADCIONA
O NOME DO APP JUNTO AOS DEMAIS QUE ESTÃO LÁ PARA SER RECONHECIDO PARA USAR NO SEU PROJETO

**Fazer migração no banco de dados(Criar banco)**
~~~ shell
python manage.py migrate
~~~


**Salvar alteracoes criadas no models.py**
~~~ shell
python manage.py makemigrations
~~~
- Após manage alterações é so rodar o codigo de migração " python manage.py migrate "


**Criar um usuario admin no django**
~~~ shell
python manage.py createsuperuser
~~~

**Rodar aplicação django**
~~~ shell
127.0.0.1:8080
~~~

**Pagina de administração**
~~~ shell
127.0.0.1:8080/admin
~~~
- depois é só logar no sistema com usuario criado