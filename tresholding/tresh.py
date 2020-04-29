import cv2
import numpy as np
from matplotlib import pyplot as plt


'''
#CELULAS SALUDABLES 
img2=cv2.imread('cel1.png',cv2.IMREAD_GRAYSCALE)
img3=cv2.imread('cel2.png',cv2.IMREAD_GRAYSCALE)


#hist = cv2.calcHist([img], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([img3], [0], None, [256], [0, 256])


#plt.plot(hist, color='gray' )
plt.plot(hist2, color='gray' )

plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')


height, width= img3.shape
for i in range(height):
    for j in range(width):
        if img3[i][j]>=185 and img3[i][j]<=188:
            img3[i][j]=255

        else:
            img3[i][j]=0
'''

#CELULAS MUERTAS
            
img2=cv2.imread('cel1.png',cv2.IMREAD_GRAYSCALE)
img3=cv2.imread('cel2.png',cv2.IMREAD_GRAYSCALE)


#hist = cv2.calcHist([img], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([img3], [0], None, [256], [0, 256])


#plt.plot(hist, color='gray' )
plt.plot(hist2, color='gray' )

plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')


height, width= img3.shape
for i in range(height):
    for j in range(width):
        if img3[i][j]<=185:
            img3[i][j]=255

        else:
            img3[i][j]=0    
#<>
#img3.resize(256,256)
cv2.imshow('celulas muertas',img3)


plt.show()
cv2.destroyAllWindows()
