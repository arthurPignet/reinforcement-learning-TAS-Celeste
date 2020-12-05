import time
import matplotlib.pyplot as plt
import d3dshot
from src.env.game_output.capture import get_celeste_region
import numpy as np

if __name__ == '__main__':
    d = d3dshot.create(capture_output="numpy")
    start_time = time.time()
    region_window = get_celeste_region('Celeste')
    d.capture(region=region_window)
    print('initialization done. ')
    time.sleep(1)

    while True:
        print('NEW_TAB')
        same_tab = True
        time.sleep(2)
        ref = d.get_latest_frame()
        plt.imshow(ref)
        plt.show()
        ref = ref[:, :, 0]
        while same_tab:
            frame = d.get_latest_frame()
            if frame[:, :, 0].mean() < 50:
                print('DEAD')
                time.sleep(2)
            else:
                if (1 - ((frame[:, :, 0] - ref) == 0)).mean() > 0.30:
                    same_tab = False
