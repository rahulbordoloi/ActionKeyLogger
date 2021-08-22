# Importing Libraries
from pynput import mouse


class mouseLogger:

    def __init__(self):
        pass

    # Function `onMove`
    def onMove(x, y):
        print(f'Pointer moved to {(x, y)}')

    # Function `onClick`
    def onClick(x, y, button, pressed):
        print(pressed, button)
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        if not pressed:
            # Stop listener
            return False

    # Function `onScroll`
    def onScroll(x, y, dx, dy):
        print('Scrolled {0} at {1}'.format(
            'down' if dy < 0 else 'up',
            (x, y)))



    # Collect events until released
    with mouse.Listener(
            on_move=onMove,
            on_click=onClick,
            on_scroll=onScroll) as listener:
        listener.join()

    # ...or, in a non-blocking fashion:
    listener = mouse.Listener(
        on_move=onMove,
        on_click=onClick,
        on_scroll=onScroll)
    listener.start()