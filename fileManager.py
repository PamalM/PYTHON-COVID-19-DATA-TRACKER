# Holds the helper methods for parsing/reading the json files.

import os
import json

# Makes the directories in the path if they don't already exist


def mkexistsdir(path):
    if not os.path.isdir(path):
        os.makedirs(path)


def exists(path):
    return os.path.exists(path)


def directoryCount(path):
    maxDayOffset = 0
    for root, dirs, files in os.walk(path):
        maxDayOffset = len(dirs)
        break
    return maxDayOffset

# Makes a preset json file with a named list if it doesn't already exist


def jsonPreset(path, listname):
    if not os.path.exists(path):
        f = open(path, "w+")
        templist = []
        tempdict = {listname: templist}
        f.write(json.dumps(tempdict))
        f.close()


def readJson(path):
    f = open(path, "r")
    data = json.loads(f.read())
    f.close()

    return data


def writeJson(path, towrite):
    f = open(path, "w")
    f.write(json.dumps(towrite))
    f.close()

# reads a list from a json file
def readList(path, listname):
    return readJson(path)[listname]

# writes a list to a json file


def writeList(path, listname, wlist):
    writeJson(path, {listname: wlist})
