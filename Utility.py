# Importing Classes and Libraries
import os
from time import asctime, localtime

# Global Vars
logFilesDirectoryPath = str(os.getcwd()) + "\Logs"
logFormatterString = '[{timeLog}]: [{logerType}]:'
currentLocalTime = asctime(localtime())


# Checking if Log Directory Exists or Not
def checkLogDir():
    if not os.path.exists(logFilesDirectoryPath):
        os.makedirs(logFilesDirectoryPath)


# Check File Size in Characters
def checkFileSize(filePath):
    with open(filePath, "r") as f:
        f.seek(0, os.SEEK_END)
        return f.tell()


