import numpy as np
import cv2
from PIL import ImageGrab

# four character code object for video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# video writer object
# out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1366, 768))
i = 0
while True:
    # capture computer screen
    img = ImageGrab.grab()
    # convert image to numpy array
    img_np = np.array(img)
    print("image")
    print(img_np.shape)
    # convert color space from BGR to RGB
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    print(frame.shape)
    # show image on OpenCV frame
    # cv2.imshow("Screen", frame)
    # write frame to video writer
    # out.write(frame)
    i += 1
    if cv2.waitKey(1) == 27:  # useful to quit the while loop
        break

# out.release()
cv2.destroyAllWindows()
