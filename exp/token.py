import datetime

def tokenGenerator(id):
    token = str(id) + str(datetime.datetime.now().timestamp())
    return token

tokenGenerator(5)