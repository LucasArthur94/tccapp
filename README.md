# Projeto de Formatura do Sistema de Gerenciamento de Disciplinas de TCC do PCS
Bem-vindos ao repositório do projeto de formatura do grupo C10, de Engenharia de Computação da Poli-USP!

## Arquitetura Básica
O sistema foi construído usando Django na versão 2.1, roda com um banco de dados (que pode ser SQLite ou PostgreSQL, dependendo do ambiente) e com uma instância do Redis para cache (em especial para suporte do Select2). Para hospedar os arquivos, foi usado o Google Drive. Por fim, para o front-end, foi usado como auxilio o MDBootstrap e também o JQuery.

## Primeiros Passos (realizados no Ubuntu 18.04)
Para você que deseja fazer manutenção ou contribuição no projeto, temos os seguintes passos.

### Pré-instalação: Instalar o Redis

[Instalação no Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04)
[Instalação no Windows](https://redislabs.com/ebook/appendix-a/a-3-installing-on-windows/a-3-2-installing-redis-on-window/)

### Instalação do Django

Requer Python > 3 e PiP (gerenciador de pacotes) instalado.

[Instruções para Download](https://www.djangoproject.com/download/)

Vale lembrar que a versão usada no projeto é a 2.1, atualizações do tipo 2.x ou superiores devem ser feitas com cautela.

### Configuração do Ambiente Virtual (Virtual Environment)

Esses passos estão no link de instalação do Django, porém vale simplificar aqui.

É saudável, para cada projeto, criar um ambiente virtual para instalar suas dependências, sem prejudicar outros projetos que possuam dependências em versões distintas. Para isso, basta criar uma vez um ambiente virtual e ativá-lo sempre que rodar o projeto.

#### No Terminal

* Para criar uma .env para o projeto (única vez): `python3 -m venv ~/.virtualenvs/<NOMEDAENV>`
* Para ativar a .env (sempre que realizar manutenções no projeto): `. ~/.virtualenvs/NOMEDAENV/bin/activate`

### Clonar Projeto

`git clone https://github.com/LucasArthur94/tccapp`

### Instalar Dependências

Com a .env ativada, ir até o diretório recém clonado e rodar:

`pip install -r requirements-dev.txt`

Este comando instalará todas as dependências do projeto.

### Aplicar as migrações no Banco de Dados

O projeto possui diversas migrações para formar a estrutura do banco de dados. Para isso, basta aplicá-las

`python manage.py migrate --run-syncdb`

Além disso, há alguns dados padrões na aplicação (de usuários e salas). Para rodar a populagem de dados:

* Dados de Usuários: `python manage.py loaddata users`
* Dados de Salas: `python manage.py loaddata rooms`

### Configurar o Google Drive

A chave `.json` não acompanha o projeto, sendo necessário gerar uma nova nos serviços de cloud do Google. Para isso, visite o site do pacote Django e siga as instruções da seção de Pré-requisitos: [google-drive-storage](https://django-googledrive-storage.readthedocs.io/en/latest/). Salve o `.json` gerado no diretório `./staticfiles/json/` como `gdrive.json`.

### Rodar o Projeto

Uma vez com as dependências instaladas e as migrações realizadas, hora de rodar o projeto:

`python manage.py runserver`

Ele subirá um servidor no endereço `localhost:8000`

Para a aplicação, é necessário também subir um servidor SMTP de E-mails. Para isso, rodar o seguinte comando:

`python -m smtpd -n -c DebuggingServer localhost:1025`

### Rodar os testes

A aplicação possui testes de funcionamento. Para rodar todos eles, basta rodar o comando:

`python manage.py test`

Vale lembrar: para os testes de interface, é necessário o [Selenium](https://www.seleniumhq.org/) instalado.

## Dúvidas?

Você pode me encontrar nas Redes Sociais:

* [Facebook](https://www.facebook.com/LucasArthur94)
* [Twitter](https://twitter.com/Lucas_Arthur_94)
* [LinkedIn](https://www.linkedin.com/in/lucasarthur/)
* [O bom e velho e-mail](mailto:lucas.arthur.felgueiras@gmail.com)
