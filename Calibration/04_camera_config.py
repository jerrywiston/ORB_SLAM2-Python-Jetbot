import numpy as np 
import cv2

npz_file = np.load('camera.npz')
ret, mtx, dist, rvecs, tvecs = npz_file['ret'], npz_file['mtx'], npz_file['dist'], npz_file['rvecs'], npz_file['tvecs']
print(mtx, dist)
print("==============================")
print("Camera.fx: " + str(format(mtx[0,0], '.8f')))
print("Camera.fy: " + str(format(mtx[1,1], '.8f')))
print("Camera.cx: " + str(format(mtx[0,2], '.8f')))
print("Camera.cy: " + str(format(mtx[1,2], '.8f')))
print()
print("Camera.k1: " + str(format(dist[0,0], '.8f')))
print("Camera.k2: " + str(format(dist[0,1], '.8f')))
print("Camera.p1: " + str(format(dist[0,2], '.8f')))
print("Camera.p2: " + str(format(dist[0,3], '.8f')))
print("Camera.k3: " + str(format(dist[0,4], '.8f')))