#FOR WSL (UBUNTU)

echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf > /dev/null

sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install python-pip

apt-get install curl
curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py
python get-pip.py

sudo apt install pipenv
pipenv install django

#CREATE A PROJECT
#pipenv shell
#django-admin startproject Swapping

#CREATE AN APPLICATION
#django-admin startapp app

pip install djangorestframework
sudo apt-get install libpq-dev
pipenv shell
pip install psycopg2
pip install python-csv
