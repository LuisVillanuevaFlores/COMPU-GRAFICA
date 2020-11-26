import cv2
import numpy as np
import matplotlib as plt
from matplotlib import pyplot as plt

img = cv2.imread("firma.jpg",0)

#########  write your code here ##################

img_out = img

hist = cv2.calcHist([img_out], [0], None, [256], [0, 256])


height, width = img_out.shape
for i in range(height):
    for j in range(width):
        if img_out[i][j]>220:
            img_out[i][j]=255
        else:
            img_out[i][j]=0
            



######## the result have to be set in img_out ####
######## not modify from here ####################

cv2.imwrite("firma_out.jpg", img_out)

    
