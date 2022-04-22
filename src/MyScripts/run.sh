cd /mnt/c/Users/Luísa/Desktop/Faculdade/MIEIC/3º\ ano/PI/Swapping/src/
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf > /dev/null
pipenv shell
python manage.py runserver

#CHECK FOR ISSUES
python manage.py check

#http://localhost:8000/