import cv2
import numpy as np
import matplotlib as plt


img = cv2.imread("question_1.png",0)


#########  write your code here ##################

#HISTOGRAM EQUALIZATION

img_out = img
hist=cv2.calcHist([img_out], [0], None, [256], [0, 256])
height, width=img_out.shape
s=[]
L=256
p_n=0
for i in range(L):
    p_n=p_n+(hist[i]/(height*width))
    s.append(((L-1)*(p_n))/1)

for i in range(height):
    for j in range(width):
        c=img_out[i][j]
        img_out[i][j]=s[c]

        
######## the result have to be set in img_out ####
######## not modify from here ####################

cv2.imwrite("question_1_sol.png", img_out)
cv2.imshow("question_1_sol.png", img_out)    
