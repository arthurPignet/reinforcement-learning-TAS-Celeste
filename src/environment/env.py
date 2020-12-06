import d3dshot
import time

import numpy as np

from .game_output.capture import get_celeste_region
from .game_input.keyboard import KeyboardToCeleste


class EnvCeleste:
    def __init__(self, frame_per_capture):
        self.frame_per_capture = frame_per_capture
        self.keyboard = KeyboardToCeleste()
        self.d = d3dshot.create(capture_output="numpy")
        region_window = get_celeste_region('src')
        self.d.capture(target_fps=30, region=region_window)
        self.keyboard.start()
        time.sleep(0.5)
        self.ref = self.d.get_latest_frame()

    def reset(self):
        self.keyboard.press('reset')

    def observation_space(self):
        frame_shape = self.d.get_latest_frame().shape
        return frame_shape + (self.frame_per_capture,)

    @staticmethod
    def is_terminal(frames):
        if np.min(frames[:, :, 0, :], axis=3).mean() < 50:
            return True
        else:
            return False

    def reward(self, frames, terminal):
        if terminal:
            time.sleep(2)
            return -100
        else:
            if (1 - ((frames[:, :, 0, -1] - self.ref) == 0)).mean() > 0.30:
                time.sleep(2)
                self.ref = self.d.get_latest_frame()
                return 200
            else:
                return -1

    def step(self, action):
        self.keyboard.press(action)
        frames = self.d.get_frame_stack(range(self.frame_per_capture), 'last')
        terminal = self.is_terminal(frames)
        reward = self.reward(frames, terminal)
        return frames, reward, terminal, {}
