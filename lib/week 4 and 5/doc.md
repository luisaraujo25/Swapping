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

https://medium.com/@frfahim/django-registration-with-confirmation-email-bb5da011e4ef


## Duvidas

Num request st1 e st2 nao deviam ser unique (chaves estrangeiras) porque assim n podem haver varios pedidos q envolvem os mesmos estudantes em turmas diferentes

adicionar constraints para st1 ser diferente de st2 e class1 ser diferente de class2


autoescape¶
Controls the current auto-escaping behavior. This tag takes either on or off as an argument and that determines whether auto-escaping is in effect inside the block. The block is closed with an endautoescape ending tag.

When auto-escaping is in effect, all variable content has HTML escaping applied to it before placing the result into the output (but after any filters have been applied). This is equivalent to manually applying the escape filter to each variable.