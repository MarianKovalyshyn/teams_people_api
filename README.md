# Teams & People API Service

This is an API for Teams & People which allows to create people and put them in teams.

## Features
* You can read, add, edit and delete people and teams.

## Installing using Docker
Docker should be installed

```shell
git clone https://github.com/MarianKovalyshyn/teams_people_api.git
cd teams_people_api/
docker-compose build
docker-compose up
```

## Installing using GitHub
Install PostgreSQL and create a database.

```shell
git clone https://github.com/MarianKovalyshyn/teams_people_api.git
cd teams_people_api/
python -m venv venv
source venv/bin/activate (MacOS)
venv\Scripts\activate (Windows)
pip install -r requirements.txt
set DB_HOST=<your_host>
set DB_NAME=<your_db_name>
set DB_USER=<your_db_user>
set DB_PASSWORD=<your_db_password>
set SECRET_KEY=<your_secret_key>
python manage.py migrate
python manage.py runserver
```

## Some examples of usage

### Creating of person and viewing of all people
![img.png](img.png)

### Detail information about person
![img_1.png](img_1.png)

### Creating of team and viewing of all teams
![img_2.png](img_2.png)

### Detail information about team
![img_3.png](img_3.png)
