import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
b=255
a=0
def contrast(name):
    fig,axs=plt.subplots(1,4)
    img1=cv2.imread(name, cv2.IMREAD_GRAYSCALE)
    axs[0].imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
    hist=cv2.calcHist([img1], [0], None, [256], [0, 256])
    axs[1].plot(hist)
    height, width=img1.shape
    l=[]
   
    for i in range(height):
        for j in range(width):
            l.append(img1[i][j])
    l.sort()
    for i in range(height):
        for j in range(width):
            img1[i][j]=(img1[i][j]-l[0])*((b-a)/(l[len(l)-1]-l[0]))+a
            
    hist1=cv2.calcHist([img1], [0], None, [256], [0, 256])
    axs[2].imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
    axs[3].plot(hist1)



def lim(hist,pixels,percent):
    c=0
    d=0
    por=pixels*percent/100
    print(por)
    i=0
    while True:
        if hist[i]>0:
            c=c+hist[i]
            if c>=por:
                c=i
                break
        i=i+1
    i=255
    while True:
        if hist[i]>0:
            d=d+hist[i]
            if d>=por:
                d=i
                break
        i=i-1
    return c,d


def outli(name,percent):

        
    fig,axs=plt.subplots(1,4)
    img1=cv2.imread(name, cv2.IMREAD_GRAYSCALE)
    for i in range(10):
        for j in range(10):
            img1[i][j]=0
            
    axs[0].imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
    hist=cv2.calcHist([img1], [0], None, [256], [0, 256])

   
    axs[1].plot(hist)
    height, width=img1.shape
    l=[]
    for i in range(height):
        for j in range(width):
            l.append(img1[i][j])
    l.sort()
    c,d=lim(hist,height*width,percent)

    print(c)
    print(d)

    for i in range(height):
        for j in range(width):
            if ((img1[i][j]-c)*((b-a)/(d-c))+a)<0:
                img1[i][j]=0
            if ((img1[i][j]-c)*((b-a)/(d-c))+a)>255:
                img1[i][j]=255
            else:
                img1[i][j]=(img1[i][j]-c)*((b-a)/(d-c))+a
            
    axs[2].imshow(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
    hist1=cv2.calcHist([img1], [0], None, [256], [0, 256])
    axs[3].plot(hist1)

    
            



#outli("contr2.jpg",10)
contrast("contr2.jpg")
plt.show()
