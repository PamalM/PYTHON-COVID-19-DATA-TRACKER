#This .py houses the helper methods for parsing/reading the json files.

import os
import json

def mkexistsdir(path):
    # Makes the directories in the path if they don't already exist
    if not os.path.isdir(path):
        os.makedirs(path)

def exists(path):
    # Returns whether or not a path in a directory exists.
    return os.path.exists(path)

def directoryCount(path):
    # Returns the # of files in a given directory.
    maxDayOffset = 0
    for root, dirs, files in os.walk(path):
        maxDayOffset = len(dirs)
        break
    return maxDayOffset

def jsonPreset(path, listname):
    # Makes a preset of json files with a named list if it doesn't already exist.
    if not os.path.exists(path):
        f = open(path, "w+")
        templist = []
        tempdict = {listname: templist}
        f.write(json.dumps(tempdict))
        f.close()

def readJson(path):
    # Reads a json into a python data structure.
    f = open(path, "r")
    data = json.loads(f.read())
    f.close()
    return data

def writeJson(path, towrite):
    # Writes a json into a python data structure.
    f = open(path, "w")
    f.write(json.dumps(towrite))
    f.close()

def readList(path, listname):
    # reads a list from a json file
    return readJson(path)[listname]

def writeList(path, listname, wlist):
    # writes a list to a json file
    writeJson(path, {listname: wlist})