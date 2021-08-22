# Importing Libraries
from pynput import mouse


# Class for Mouse Logger
class mouseLogger:

    # Default Constructor
    def __init__(self):
        pass

    # Method `onMove`
    @staticmethod
    def onMove(x, y):
        print(f'Pointer moved to {(x, y)}')

    # Function `onClick`
    @staticmethod
    def onClick(x, y, button, pressed):
        print(pressed, button)
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))

        # Stop Listener
        if not pressed:
            return False

    # Method `onScroll`
    @staticmethod
    def onScroll(x, y, dx, dy):
        print('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up',
            (x, y)))

    # Method `runMouseLogger`
    """
        Main Driver Code for Listener and Release
    """
    def runMouseLogger(self):

        with mouse.Listener(
                on_move = mouseLogger.onMove,
                on_click = mouseLogger.onClick,
                on_scroll = mouseLogger.onScroll) as listener:
            listener.join()
        with mouse.Listener(
                on_move = mouseLogger.onMove,
                on_click = mouseLogger.onClick,
                on_scroll = mouseLogger.onScroll) as listener:
            listener.start()

