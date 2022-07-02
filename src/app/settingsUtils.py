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


def setAllowance(enabled, reqType):
    
    currentDict = getCurrentSettings()

    strType = ""

    if reqType == "duo":
        strType = "duoReqEnabled"
    elif reqType == "single":
        strType = "singleReqEnabled"

    currentDict[strType] = enabled
    jsonObj = json.dumps(currentDict, indent = 2)
    jsonFile = open("app/files/adminSettings.json", "w+")
    jsonFile.write(jsonObj)


def getAllowance(reqType):

    if reqType == "duo":
        strType = "duoReqEnabled"
    elif reqType == "single":
        strType = "singleReqEnabled"

    jsonFile = open("app/files/adminSettings.json", "r")
    jsonObj = json.load(jsonFile)
    
    enabled = jsonObj[strType]

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