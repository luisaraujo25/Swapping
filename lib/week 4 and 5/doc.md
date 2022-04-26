# Load Data

https://docs.djangoproject.com/en/4.0/ref/django-admin/

`python manage.py dumpdata`

`python manage.py loaddata`

# Create object

`john = Author.objects.create(name="John")`

# Error with "__str__ returned non-string (type int)" solved

<code>
def __str__(self):
        return str(self.number)
</code>