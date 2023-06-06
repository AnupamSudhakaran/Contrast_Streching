import cv2;
import math
import matplotlib.pyplot as plt
img=cv2.imread('download.jpg');

cv2.imshow('Real',img);
n,m,c=img.shape

img1=img;




def funct_max(img,i,j,channel):
    l1=[]
    n,m,h=img.shape;

    l1.append(img[i,j][channel]);
    l1.append(img[min(i+1,n-1),j][channel]);
    l1.append(img[max(i-1,0),j][channel]);
    l1.append(img[i,min(j+1,m-1)][channel]);
    l1.append(img[i,max(j-1,0)][channel]);

#
    l1.append(img[min(i+1,n-1),min(j+1,m-1)][channel]);#i+1,j-1
    l1.append(img[max(i-1,0),min(j+1,m-1)][channel]);#i+1,j-1
    l1.append(img[min(i+1,n-1),max(j-1,0)][channel]);#i+1,j-1
    l1.append(img[min(i-1,0),max(j-1,0)][channel]);#i+1,j-1
    
    
    return max(l1)


def funct_min(img,i,j,channel):
    l1=[]
    n,m,h=img.shape;

    l1.append(img[i,j][channel]);
    l1.append(img[min(i+1,n-1),j][channel]);
    l1.append(img[max(i-1,0),j][channel]);
    l1.append(img[i,min(j+1,m-1)][channel]);
    l1.append(img[i,max(j-1,0)][channel]);

#
    l1.append(img[min(i+1,n-1),min(j+1,m-1)][channel]);#i+1,j-1
    l1.append(img[max(i-1,0),min(j+1,m-1)][channel]);#i+1,j-1
    l1.append(img[min(i+1,n-1),max(j-1,0)][channel]);#i+1,j-1
    l1.append(img[min(i-1,0),max(j-1,0)][channel]);#i+1,j-1
    
    
    return min(l1)



for i in range(n):
    for j in range(m):
        
        img[i,j][0]=((((img[i,j][0]-funct_min(img,i,j,0))/(funct_max(img,i,j,0)-funct_min(img,i,j,0)))*255)**0.7)%255
        img[i,j][1]=((((img[i,j][1]-funct_min(img,i,j,1))/(funct_max(img,i,j,1)-funct_min(img,i,j,1)))*255)**0.7)%255
        img[i,j][2]=((((img[i,j][2]-funct_min(img,i,j,2))/(funct_max(img,i,j,2)-funct_min(img,i,j,2)))*255)**0.7)%255




cv2.imshow("modfied",img);
cv2.waitKey(0)
cv2.destroyAllWindows()