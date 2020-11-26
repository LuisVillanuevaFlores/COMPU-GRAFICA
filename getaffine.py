import cv2
from matplotlib import pyplot as plt
import numpy as np
import math 

'''
def oper(M,img,hei,wei):
    h,w,c=img.shape
    img_out=np.zeros((hei,wei,c),np.uint8)
    iden=np.array([[M[1][1],M[1][0]],[M[0][1],M[0][0]]])
    B=np.array([[M[1][2]],[M[0][2]]])
    for i in range(h):
        for j in range(w):
            vector=np.array([[i],[j]])
            aux=img[i][j]
            res=np.dot(iden,vector)+B
            res=res.astype(int)
            if(res[0][0]<img_out.shape[0] and res[0][0]>=0):
                if(res[1][0]<img_out.shape[1] and res[1][0]>=0):
                    img_out[res[0][0]][res[1][0]]=aux

                    
    return img_out
'''

def oper(M,img,hei,wei):
    X=[0,0]
    h,w,c=img.shape
    img_out=np.zeros((hei,wei,c),np.uint8)
    iden=np.array([[M[1][1],M[1][0]],[M[0][1],M[0][0]]])
    B=np.array([[M[1][2]],[M[0][2]]])
    for i in range(hei):
        for j in range(wei):
            vector=np.array([[i],[j]])
            Y=vector-B
            X=cv2.solve(iden,Y)
            #print(X)
            x=int(X[1][0][0])
            y=int(X[1][1][0])
            #print(x,y)
            if(x<img_out.shape[0] and x>=0):
                if(y<img_out.shape[1] and y>=0):
                    print(x,y,"---",i,j)
                    img_out[i][j]=img[x][y]

                    
    return img_out


#ROTACION
img= cv2.imread('jesse.jpg')
angu=math.radians(65)
f,c,x=img.shape
M=np.array([[math.cos(angu), math.sin(angu), (1 - math.cos(angu)) * c/2 - math.sin(angu) * f/2], [-math.sin(angu), math.cos(angu), math.sin(angu) * c/2 + (1 - math.sin(angu)) * f/2]])
res = oper(M,img,f,c)
cv2.imwrite('mirota.jpg',res);
M2 = np.float32([[math.cos(angu), math.sin(angu), (1 - math.cos(angu)) * c/2 - math.sin(angu) * f/2], [-math.sin(angu), math.cos(angu), math.sin(angu) * c/2 + (1 - math.sin(angu)) * f/2]])
cv2.imwrite('cv_rotate.jpg',cv2.warpAffine(img, M2, (c, f)))

'''
#Esala

img= cv2.imread('jesse.jpg')
f,c,x=img.shape
M=np.array([[2,0,0],[0,0.5,0]])
res = oper(M,img,int(f/2),int(c*2))
dst=cv2.warpAffine(img, M, (c*2, int(f/2)))
#Warpaffine
cv2.imshow('escalecv.jpg',dst)
#Función propia
cv2.imshow('miescale.jpg',res)
'''
