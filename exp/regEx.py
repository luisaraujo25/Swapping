import re

mail = input()

valid = re.search("^up.{9}@fe.up.pt$", mail)

if valid == None:
    print("Invalid E-mail")
else:
    print(mail)