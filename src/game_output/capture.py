from multiprocessing import Queue, Process

import numpy as np
import cv2
import win32gui
from PIL import ImageGrab

# four character code object for video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')


# video writer object

class GameCapture:
    screen_name = 'Celeste'

    def __init__(self, save=False, **kwargs):
        self.save = save
        if self.save:
            self.file_out = cv2.VideoWriter(kwargs.get('path', "./output.avi"), fourcc, 5.0, (1366, 768))
        self.output_queue = Queue()
        self.celeste_window = self._get_screens()
        self.process = Process(target=self.game_capture, args=(self.output_queue,self.celeste_window))

    def start(self):
        self.process.start()

    def kill(self):
        self.process.kill()
        cv2.destroyAllWindows()

    def _read(self):
        return self.output_queue.get()

    def read(self):
        frame = self._read()
        if self.save:
            self.file_out.write(frame)
        return frame

    def shown(self):
        cv2.imshow("window", self.read())

    def stream(self):
        while True:
            self.shown()
            if cv2.waitKey(1) == 27:  # useful to quit the while loop
                break

    def _get_screens(self):
        def enum_cb(hwnd, result_list):
            result_list.append((hwnd, win32gui.GetWindowText(hwnd)))

        # wait for the program to start initially.
        winlist = []
        win32gui.EnumWindows(enum_cb, winlist)
        screens = [(hwnd, title) for hwnd, title in winlist if self.screen_name in title.lower()]
        while len(screens) == 0:
            screens = [(hwnd, title) for hwnd, title in winlist if self.screen_name in title.lower()]
            win32gui.EnumWindows(enum_cb, winlist)

        return screens

    @staticmethod
    def game_capture(queue_out, window):
        window_box = win32gui.GetWindowRect(window)
        while True:
            # capture computer screen
            img = ImageGrab.grab(bbox=window_box)
            # convert image to numpy array
            img_np = np.array(img)
            # convert color space from BGR to RGB
            frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            queue_out.put(frame)
