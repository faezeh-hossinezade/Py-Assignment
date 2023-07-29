import cv2
import numpy as np
# from PIL import Image


image=cv2.imread("bat.jpg")

image2=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
rows,cols=image2.shape

_,image3=cv2.threshold(image2,140,255,cv2.THRESH_BINARY_INV)
cv2.putText(image3,"BATMAN",(370,500),cv2.FONT_HERSHEY_DUPLEX
           ,2,255,3)
cv2.imshow("batprime",image3)
cv2.waitKey()