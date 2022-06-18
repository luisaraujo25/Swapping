import json

def setTimeout(timeout):
    
    currentDict = getCurrentSettings()

    currentDict['updatedTimeout'] = int(timeout)

    jsonObj = json.dumps(currentDict, indent = 2)
    jsonFile = open("app/files/adminSettings.json", "w+")
    jsonFile.write(jsonObj)

def getTimeout():

    jsonFile = open("app/files/adminSettings.json", "r")
    jsonObj = json.load(jsonFile)

    timeout = jsonObj['updatedTimeout']

    return timeout


def setAllowance(enabled):
    
    currentDict = getCurrentSettings()

    currentDict['requestsEnabled'] = enabled

    jsonObj = json.dumps(currentDict, indent = 2)
    jsonFile = open("app/files/adminSettings.json", "w+")
    jsonFile.write(jsonObj)


def getAllowance():

    jsonFile = open("app/files/adminSettings.json", "r")
    jsonObj = json.load(jsonFile)

    enabled = jsonObj['requestsEnabled']

    return enabled

def getEmailUser():

    jsonFile = open("app/files/PERSONALDATA.json", "r")
    jsonObj = json.load(jsonFile)
    return jsonObj['email']

def getEmailPassword():

    jsonFile = open("app/files/PERSONALDATA.json", "r")
    jsonObj = json.load(jsonFile)
    return jsonObj['password']

def getCurrentSettings():

    jsonFile = open("app/files/adminSettings.json", "r")
    jsonObj = json.load(jsonFile)

    return jsonObj