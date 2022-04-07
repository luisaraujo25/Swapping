import re

mail = input()

valid = re.search("^up[0-9]{3}@.+\.up\.pt$", mail)

if valid == None:
    print("Invalid E-mail")
else:
    print(mail)
