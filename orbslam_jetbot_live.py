#!/usr/bin/env python3
import sys
import os.path
import orbslam2
import time
import cv2
from jetbot import Camera

def main(vocab_path, settings_path):
    slam = orbslam2.System(vocab_path, settings_path, orbslam2.Sensor.MONOCULAR)
    slam.set_use_viewer(True)
    slam.initialize()

    camera = Camera.instance(width=960, height=540, capture_width=1280, capture_height=720)
    print('-----')
    print('Start processing sequence ...')
    ts = 0
    #cv2.namedWindow("test")
    while(True):
        img = camera.value.copy()

        t1 = time.time()
        slam.process_image_mono(img, float(ts))
        t2 = time.time()

        ttrack = t2 - t1
        print("frame id:" + str(ts), ttrack)
        time.sleep(0.01)
        ts += 1

    save_trajectory(slam.get_trajectory_points(), 'trajectory.txt')
    slam.shutdown()
    return 0

def save_trajectory(trajectory, filename):
    with open(filename, 'w') as traj_file:
        traj_file.writelines('{time} {r00} {r01} {r02} {t0} {r10} {r11} {r12} {t1} {r20} {r21} {r22} {t2}\n'.format(
            time=repr(stamp),
            r00=repr(r00),
            r01=repr(r01),
            r02=repr(r02),
            t0=repr(t0),
            r10=repr(r10),
            r11=repr(r11),
            r12=repr(r12),
            t1=repr(t1),
            r20=repr(r20),
            r21=repr(r21),
            r22=repr(r22),
            t2=repr(t2)
        ) for stamp, r00, r01, r02, t0, r10, r11, r12, t1, r20, r21, r22, t2 in trajectory)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
