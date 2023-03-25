import cv2
import time
from toupcam import ToupCamCamera
import matplotlib.pyplot as plt
import skimage.io as io
##################
#Parameter
EXPOSURE = 5*(10**3)
GAIN = 100
#########

cam = ToupCamCamera(resolution_number=1)
cam.open()


cam.set_auto_exposure(0)
cam.set_exposure_time(EXPOSURE)
cam.set_brightness(GAIN)

print(cam.get_resolution_list())

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

while (True):
    im = cam.get_cv2_image()
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    io.imsave('image.jpg', im)
    cv2.imshow('image', im)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

time.sleep(0.20)
im = cam.get_cv2_image()
plt.imshow(im)
plt.imsave(im, 'image.jpg')


cam.close()