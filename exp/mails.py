import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "qfabray300@gmail.com"  # Enter your address
receiver_email = "lmpa.pt@gmail.com"  # Enter receiver address
password = ""
message = """\
Subject: Class swap


I don't accept accents."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


#host.com/user/email/{code}/confirm USAR ISTO PARA CRIAR O LINK DE CONFIRMAÇAO
# https://stackoverflow.com/questions/32086740/how-you-create-confirmation-link-for-email