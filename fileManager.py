import os
import json

#Makes the directories in the path if they don't already exist
def mkexistsdir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

#Makes a preset json file with a named list if it doesn't already exist
def jsonPreset(path, listname):
    if not os.path.exists(path):
        f = open(path,"w+")
        templist = []
        tempdict = {listname:templist}
        f.write(json.dumps(tempdict))
        f.close()

#reads a list from a json file
def readList(path,listname):
    f = open(path,"r")
    templist = json.loads(f.read())[listname]
    f.close()

    return templist

#writes a list to a json file
def writeList(path,listname,wlist):
    f = open(path,"w")
    f.write(json.dumps({listname:wlist}))
    f.close()