# Importing Libraries
from KeyboardLogger import keyBoardLogger
from MouseLogger import mouseLogger
from multiprocessing import Process

# Main Method
if __name__ == '__main__':

    """
    To Terminate the Program:
        1. Press `esc` via Keyboard.
        2. Press Middle Mouse Button.
    """

    try:

        # Keyboard Logger
        process1 = Process(target = keyBoardLogger.runKeyBoardLogger)
        process1.start()

        # Mouse Logger
        process2 = Process(target = mouseLogger().runMouseLogger)
        process2.start()

    except:
        print("Exception Message: Program Safely Terminated!")
