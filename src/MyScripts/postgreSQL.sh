sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
#sudo apt-get install postgresql
sudo apt-get install postgresql-12

#https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-20-04
#https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8
#https://www.digitalocean.com/community/tutorials/como-instalar-e-configurar-o-pgadmin-4-no-modo-servidor-pt

#I NEEDED THE FOLLOWING COMMAND SINCE I COULDNT CONNECT TO THE SERVICE
sudo service postgresql restart
sudo service postgresql start

sudo -i -u postgres
#TO ACCESS POSTGRESQL PROMPT:
psql
#TO QUIT PROMPT:
\q

#INSTALLED VERSION: PostgreSQL 12.9

#pgadmin error
ALTER USER postgres PASSWORD '.';

#AFTER CREATING A CLASS IN MODELS:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

#SEE TABLES
\dt

#SEE DB
\l

#SEE TABLES
python manage.py sqlmigrate app 0001

#DROP TABLES AND "REFRESH" WHEN MIGRATING IS NOT UPDATING
DROP TABLE {app_name}_{model_name}
python manage.py migrate app zero
python manage.py migrate --fake-initial