import os
import cv2
from jetbot import Camera

dataset_path = "jetbot_dataset_960test2/"
image_folder = "rgb/"
if not os.path.exists(dataset_path+image_folder):
    os.makedirs(dataset_path+image_folder)
file = open(dataset_path+"rgb.txt", "w")

camera = Camera.instance(width=960, height=540, capture_width=1280, capture_height=720)
iid = 0
while(True):
    img = camera.value    
    cv2.imshow("test", img)
    
    fname = str(iid).zfill(4) + ".jpg"
    cv2.imwrite(dataset_path + image_folder + fname, img)
    # Write file
    file.write(str(iid) + " " + image_folder + fname + "\n")

    iid += 1
    k = cv2.waitKey(100)
    if k == ord('q'):
        camera.stop()
        break
