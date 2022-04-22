from django.core import mail

connection = mail.get_connection()

connection.open()

email = EmailMessage(
    'Title',
    'Body',
    'qfabray300@gmail.com',
    ['lmpa.pt@gmail.com'],
    []
)

email.send(fail_silently=False)

connection.close()