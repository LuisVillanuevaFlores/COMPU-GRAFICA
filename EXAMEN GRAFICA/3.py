import cv2
import numpy as np
#import matplotlib as plt
from matplotlib import pyplot as plt


img = cv2.imread("question_3.png",0)

#########  write your code here ##################

#Profesor estaba probando a ver si me salía , y decidí mandarlo a ver si lo
#podría considerar como intento


img_out = cv2.imread("question_3.png",0)
height, width = img_out.shape
for i in range(height):
    for j in range(width):
        c1=0
        c2=0
        for x in range(i-1,i+2):
            for y in range(j-1,j+2):
                if (x!=i and y!=j) or (x==i and y!=j) or (x!=i and y==j):
                    if((x>=0 and y>=0) and (x<height and y<width)):
                        c1=c1+img[x][y]
                        c2=c2+1
        c1=c1/c2-2

        if(img_out[i][j]>c1):
            img_out[i][j]=255
        else:
            img_out[i][j]=0
                
            
    

######## the result have to be set in img_out ####
######## not modify from here ####################

cv2.imwrite("question_3_sol.png", img_out)
    
