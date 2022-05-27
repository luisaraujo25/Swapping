import re

mail = input()

valid = re.search("^up[0-9]{9}@.+\.up\.pt$", mail)

if valid == None:
    print("Invalid E-mail")
else:
    print(mail)
