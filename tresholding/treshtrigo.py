import cv2
import numpy as np
from matplotlib import pyplot as plt

img3 = cv2.imread('trigo.png')


color = ('b','g','r')

for i, c in enumerate(color):
    hist = cv2.calcHist([img3], [i], None, [256], [0, 256])
    plt.plot(hist, color = c)
    plt.xlim([0,256])

height, width , canal= img3.shape
for i in range(height):
    for j in range(width):
            if img3[i][j][0]<=121 or img3[i][j][1]<=144 or img3[i][j][2]<=184:
                img3[i][j][0]=0
                img3[i][j][1]=0
                img3[i][j][2]=0

'''

if img3[i][j][0]>0 and img3[i][j][0]<46:
                img3[i][j][0]=0
                img3[i][j][1]=0
                img3[i][j][2]=0
            if img3[i][j][1]>175 and img3[i][j][1]<250:
                img3[i][j][0]=0
                img3[i][j][1]=0
                img3[i][j][2]=0
            if img3[i][j][1]>210 and img3[i][j][1]<260:
                img3[i][j][0]=0
                img3[i][j][1]=0
                img3[i][j][2]=0      
                         
'''

        
cv2.imshow('trigo',img3)
plt.show()

cv2.destroyAllWindows()
