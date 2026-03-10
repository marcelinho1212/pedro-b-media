README.md
Pedro Barbosa Media Website

Website institucional desenvolvido em Django para apresentação de serviços de produção audiovisual.

Tecnologias

Python

Django

HTML

CSS

JavaScript

PostgreSQL

Gunicorn

WhiteNoise

Instalação

Clone o repositório:

git clone https://github.com/seu-repo/pedro-b-media.git

Entre na pasta:

cd pedro-b-media

Crie o ambiente virtual:

python -m venv venv

Ative o ambiente:

Windows

venv\Scripts\activate

Mac / Linux

source venv/bin/activate

Instale as dependências:

pip install -r requirements.txt
Variáveis de Ambiente

Crie um arquivo .env:

EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
CONTACT_RECEIVER_EMAIL=
SECRET_KEY=
DEBUG=True
Migrações
python manage.py migrate
Rodar servidor local
python manage.py runserver

Acesse:

http://127.0.0.1:8000
Deploy

Deploy realizado na plataforma Render.

Build command:

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate

Start command:

gunicorn config.wsgi:application