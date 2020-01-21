# Categories API
## Description
Create a simple Categories API that stores category tree to database and returns category parents, children and siblings by category id.
## Requirements
Use Python 3.4+ and Django Framework (or Django Rest Framework).
__Use of any other third-party libraries or Django extensions (mptt, treebread, etc) is prohibited.__
## Installation
### Envfile
Rename tmpl.env to .env and fill required data
- SECRET_KEY -> django secret
- DEBUG -> Django debug setting 1/0

### Docker-compose
~~~
docker-compose build
docker-compose up
~~~
Access localhost

### Virtualenv
~~~
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
~~~
Access localhost:8000