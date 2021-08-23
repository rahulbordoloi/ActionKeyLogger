# Importing Libraries
from pynput import mouse
from Utility import checkLogDir, checkFileSize, logFormatterString, currentLocalTime, mouseBtnActionToText
from time import time


# Class for Mouse Logger
class mouseLogger:

    # Class Variables
    __count, __actions = 0, []
    _startTime, _endTime = 0.0, 0.0

    # Default Constructor
    def __init__(self):
        pass

    # Method `onMove`
    """
        Record the Mouse Movements Actions
    """
    @classmethod
    def __onMove(cls, x, y):

        ## Mouse Action Taken
        actionTaken = f'Pointer moved to {(x, y)}'

        ## Appending Keys and Changing the Count
        cls.__actions.append(actionTaken)
        cls.__count += 1

    # Function `onClick`
    """
        Record the Mouse Clicking Actions
    """
    @classmethod
    def __onClick(cls, x, y, button, pressed):

        ## Mouse Action Taken
        actionTaken = '{0} {1} at {2}'.format(
            'Pressed' if pressed else 'Released',
            mouseBtnActionToText(str(button)),
            (x, y))

        ## Appending Keys and Changing the Count
        cls.__actions.append(actionTaken)
        cls.__count += 1

        # Stop Listener if Middle Mouse Button is Pressed
        if str(button) == 'Button.middle':
            cls.__writeFile()
            return False

    # Method `onScroll`
    """
        Record the Mouse Scrolling Actions
    """
    @classmethod
    def __onScroll(cls, x, y, dx, dy):

        ## Mouse Action Taken
        actionTaken = 'Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up',
            (x, y))
        ## Appending Keys and Changing the Count
        cls.__actions.append(actionTaken)
        cls.__count += 1

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
        filePath = f"Logs\\MouseLog {str(timeForFile)}.txt"
        with open(filePath, "w") as file:
            fileSize = checkFileSize(filePath)
            if fileSize >= (10 ** 5):  # 100 KB
                cls.__writeFile()
            else:
                file.write(logFormatterString.format(timeLog = currentLocalTime, logerType = "Mouse"))
                file.write("\n")
                for action in cls.__actions:
                    cls._endTime = time()
                    if cls._endTime - cls._startTime > 60:
                        file.write(logFormatterString.format(timeLog = currentLocalTime, logerType = "Mouse"))
                        file.write("\n")
                        cls._startTime = time()
                    file.write(action + "\n")
                finalText = f"\n\nTotal Mouse Actions: {cls.__count}"
                file.write(finalText)

    # Method `runMouseLogger`
    """
        Main Driver Code for Listener and Release
    """
    @classmethod
    def runMouseLogger(cls):

        # Collecting Events until Released
        cls._startTime = time()
        with mouse.Listener(
                on_move = cls.__onMove,
                on_click = cls.__onClick,
                on_scroll = cls.__onScroll) as listener:
            listener.join()

