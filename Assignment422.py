import cv2 
import numpy as np
import imageio

image=cv2.imread("television.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#521*758
image_lst = []
while True:
    
    image2=np.random.random(size =(800, 1000))*255
    image3=np.array(image2,dtype=np.int8)
    barfak=image3[45:430,50:560]
    image[45:430,50:560]=barfak
    images=image.astype(np.uint8)
    image_lst.append(images)
    cv2.imshow("tv",image)
    if cv2.waitKey(25) & 0xFF == ord ('q'):
       break


cv2.waitKey()


exportname = "E:/pylearn/processing/test.gif"
kargs = { 'duration': 0.1 }
imageio.mimsave(exportname, image_lst,**kargs)


