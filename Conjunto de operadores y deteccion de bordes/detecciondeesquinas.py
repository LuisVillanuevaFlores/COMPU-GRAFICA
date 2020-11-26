import numpy as np
import cv2

img = cv2.imread('resultado.png')
#img = cv2.resize(img, (500,500))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 4, 0.01, 200)
corners = np.int0(corners)
print(corners)
f = open ('puntos.txt','w')

h,w,c=img.shape

for i in range(4):
    if int(corners[i][0][0]) > h/2 and int(corners[i][0][1] > w/2):
        punto1=(corners[i][0][0],corners[i][0][1])
 
    elif int(corners[i][0][0]) > w/2 and int(corners[i][0][1] < h/2):
        punto2=(corners[i][0][0],corners[i][0][1])
        
    elif int(corners[i][0][0]) < w/2 and int(corners[i][0][1] < h/2):
        punto3=(corners[i][0][0],corners[i][0][1])
    else:
        punto4=(corners[i][0][0],corners[i][0][1])


print(punto1)
print(punto2)
print(punto3)
print(punto4)
    
    

print(h,w)


f.write(str(punto1[0]))
f.write(",")
f.write(str(punto1[1]))
f.write(",")
f.write(str(punto2[0]))
f.write(",")
f.write(str(punto2[1]))
f.write(",")
f.write(str(punto3[0]))
f.write(",")
f.write(str(punto3[1]))
f.write(",")
f.write(str(punto4[0]))
f.write(",")
f.write(str(punto4[1]))
f.close()



   
cv2.imshow('corner', img)
cv2.waitKey(0)
