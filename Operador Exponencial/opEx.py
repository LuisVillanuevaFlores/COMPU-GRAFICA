import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math

def exponencial(inp,bconst,constante,res):
    f,c=inp.shape
    for i in range(f):
        for j in range(c):
            r=constante*(pow(bconst,inp[i][j])-1)
            if(r<0):
                inp[i][j]=0
            elif(r>255):
                inp[i][j]=255
            else:
                inp[i][j]=r
    cv.imshow(res,inp)

def rtopowe(inp,constant, rconstant,res):
    f,c=inp.shape
    for i in range(f):
        for j in range(c):
            g=constant*(pow(inp[i][j],rconstant))
            if(g<0):
                inp[i][j]=0
            elif(g>255):
                inp[i][j]=255
            else:
                inp[i][j]=g
    cv.imshow(res,inp)

    
a = cv.imread('log_6.jpg',0)
b=cv.imread('log_6.jpg',0)
c=cv.imread('log_6.jpg',0)
#exponencial(a,1.01,20,'res1')
#exponencial(b,1.01,10,'res2')
#exponencial(c,1.01,5,'res3')
rtopowe(a,0.05,1.5,'x')
rtopowe(b,0.1,1.5,'y')
rtopowe(c,0.01,1.5,'z')
