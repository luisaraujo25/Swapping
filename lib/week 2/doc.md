# Documentation from Week 2

## Admin

One of Django's most popular features are administrators.
To create one admin (SuperUser) it was used:

`python manage.py createsuperuser`

Username: admin

E-mail address: lmpa.pt@gmail.com

Password: luisaaraujo

## UML

![uml](uml.png)

## State Diagram for Requests

![Request State Diagram](statediagram.jpg)

## Relational

student(<u>id</u>, e-mail, name, up)


## Django Models

After linking a database we need to migrate it.
This can be done using the following command:

`python manage.py migrate`

Using models we can create tables for our database.
After creating a model we need to use the command :

`python manage.py makemigrations`

In the folder app/migrations you can notice a new file was added (for example: "0001_initial.py").
Everytime we make migrations no file will be automatically deleted, even if we just changed one attribute of a table a new file will be created with all changes.
"By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration."

### Fiels

CharField vs TextField

CharField has a length limit (255). So when we need name, emails, etc, inputs CharField is a better choice to ensure more accuracy to the data we are receiving.

<hr>

## Problems

- CSS files not working properly

Details:
Everytime I update, let's say, the background color, no changes would happen.

<b> FIXED: </b>

The problem was in chrome. When I tried localhost on microsoft edge everything work properly.
https://stackoverflow.com/questions/47415844/django-css-works-on-chrome-but-not-firefox


