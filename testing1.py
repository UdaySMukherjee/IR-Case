# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 12:33:45 2022

@author: USER
"""

import cv2
import numpy as np

img_path =r"C:\\Users\\USER\\Desktop\\IR_Case_006.png"

def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("Threshold1","Parameters",250,255,empty)
cv2.createTrackbar("Threshold2","Parameters",200,255,empty)


def getContours(img,imgContour):
    contour,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    for cnt in contour:
        area=cv2.contourArea(cnt)
        if area>1000:
            cv2.drawContours(imgContour,cnt,-1,(255,0,255),7)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            x,y,w,h=cv2.boundingRect(approx)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),5)
            
        
      

img = cv2.imread(r"C:\\Users\\USER\\Desktop\\IR_Case_006.png",0)
img = cv2.medianBlur(img,5)
img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
img = cv2.resize(img, (480, 360),interpolation=cv2.INTER_CUBIC)
cv2.imshow("sample Image", img)

imgContour=img.copy()
imgBlur=cv2.GaussianBlur(img,(7,7),1)
#imgGray=cv2.cvtColor(imgBlur,cv2.COLOR_BGR2GRAY)
    
threshold1=cv2.getTrackbarPos("Threshold1","Parameters")
threshold2=cv2.getTrackbarPos("Threshold2","Parameters")
imgCanny=cv2.Canny(img,threshold1,threshold2)
    
kernel=np.ones((2,2))
imgDil=cv2.dilate(imgCanny,kernel,iterations=1)
kernel=np.ones((2,2))
img_erosion = cv2.erode(imgDil, kernel, iterations=1)  
getContours(imgDil, imgContour)
    

cv2.imshow("Result 3",imgCanny)
cv2.imshow("Result 4",imgDil)
cv2.imshow("Result 5",img_erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()