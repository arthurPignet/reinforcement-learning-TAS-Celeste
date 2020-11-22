import time
import cv2
from src.game_output.capture import GameCapture

def shown(frame):
  cv2.imshow("window", frame)
  cv2.waitKey()

if __name__ == '__main__':
    capturator = GameCapture()
    capturator.start()

    start_time = time.time()
    history_frames = []
    for nb_frame in range(100):
        history_frames.append(capturator.read())
    print(f"100 frames captured in {time.time() - start_time} s.")
    capturator.kill()
    shown(history_frames[0])


