from multiprocessing import Queue, Process

from keyboard import press_and_release


class KeyboardToCeleste:
    # map the keyboard according to celeste
    right = 'q'
    left = 'd'
    up = 'z'
    down = 's'
    jump = 'j'
    confirm = 'j'
    jump2 = 'k'
    dash = 'x'
    talk = 'x'
    dash2 = 'c'
    grab = 'g'
    pause = 'p'
    reset = 'a'

    def __init__(self):
        self.input_queue = Queue()
        self.process = Process(target=self.send_input, args=(self.input_queue,))

    def start(self):
        self.process.start()

    def kill(self):
        self.input_queue.put('STOP')

    def press(self, *inputs):
        for input in inputs:
            self.input_queue.put(str(input))

    @staticmethod
    def send_input(queue_in):
        """
        Will be run in a parallel process, waiting for keys and pressing them
        :param queue_in: Queue(). It must contain str of this kind : 'ctrl+c, a'
        """

        for hot_keys in iter(queue_in.get, 'STOP'):
            press_and_release(hot_keys)

    def controls_map(self):
        pass
