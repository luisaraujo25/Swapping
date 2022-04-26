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

## Send emails

email: swappingfeup@gmail.com
passe: swapclasses

## Duvidas

Num request st1 e st2 nao deviam ser unique (chaves estrangeiras) porque assim n podem haver varios pedidos q envolvem os mesmos estudantes em turmas diferentes

adicionar constraints para st1 ser diferente de st2 e class1 ser diferente de class2
