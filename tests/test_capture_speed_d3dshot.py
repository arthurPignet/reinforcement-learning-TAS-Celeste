import time
import numpy as np
import cv2
import d3dshot
from src.game_output.capture import get_celeste_region

def shown(frame):
    cv2.imshow("window", frame)
    cv2.waitKey()


if __name__ == '__main__':
    d = d3dshot.create(capture_output="numpy")
    start_time = time.time()
    region_window = get_celeste_region('src')
    d.capture(region=region_window)
    time.sleep(1)
    history_frames = []
    for nb_frame in range(100):
        history_frames.append(d.get_latest_frame())
    d.stop()
    print(f"100 frames captured in {time.time() - start_time} s.")
    shown(history_frames[0])
