import numpy as np
import win32gui


# video writer object

def get_celeste_region(window_name='Celeste'):
    celeste_window_id = win32gui.FindWindow(None, window_name)
    return win32gui.GetWindowPlacement(celeste_window_id)[-1]