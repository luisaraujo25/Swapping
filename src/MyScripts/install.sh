#FOR WSL (UBUNTU)

#echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf > /dev/null
sudo apt install pipenv
pipenv install django

#CREATE A PROJECT
#pipenv shell
#django-admin startproject Swapping

#CREATE AN APPLICATION
#django-admin startapp app