import time
import cv2
import imageio
import numpy as np

rows = np.random.random((1,500))*666
cols = [i for i in range(1,1000,2)]
rows = np.array(rows , dtype=np.uint0)
cols = np.array(cols , dtype=np.uint0)
images = []

while True:
    img = cv2.imread('winter.jpg')
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    for i in range(500):
        r = int(rows[0][i])
        c = int(cols[i])
        img[r:int(r+3),c:int(c+3)] = 255   

    for i in range(500):
        rows[0][i] = rows[0][i] + 200
        if rows[0][i] > 600:
            rows[0][i] = rows[0][i]-600

    cv2.imshow('',img)
    time.sleep(0.3)
    images.append(img)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

imageio.mimsave('winter.gif',images)