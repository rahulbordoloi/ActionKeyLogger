# Importing Libraries
from KeyboardLogger import keyBoardLogger
from MouseLogger import mouseLogger


# Main Method
if __name__ == '__main__':

    """
    To Terminate the Program:
        1. Press `esc` via Keyboard.
        2. Press Middle Mouse Button.
    """

    try:

        # Keyboard Logger
        keyBoardLogger.runKeyBoardLogger()

        # Mouse Logger
        mouseLogger().runMouseLogger()

    except:
        print("Exception Message: Program Safely Terminated!")
