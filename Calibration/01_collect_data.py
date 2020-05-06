import os
import cv2
from jetbot import Camera

image_folder = "Images/"
if not os.path.exists(image_folder):
    os.makedirs(image_folder)
camera = Camera.instance(width=960, height=540, capture_width=1280, capture_height=720)
iid = 0
while(True):
    img = camera.value    
    cv2.imshow("test", img)
    fname = str(iid).zfill(4) + ".jpg"
    cv2.imwrite(image_folder + fname, img)
    iid += 1
    k = cv2.waitKey(200)
    if k == ord('q'):
        break

