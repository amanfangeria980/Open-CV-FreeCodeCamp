# Essential Functions in OpenCV
from xmlrpc.client import INTERNAL_ERROR
import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')

cv.imshow('Park Window',img)

# Converting to GrayScale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grey',gray)

# Blur Image
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# Edge Cascade 
canny=cv.Canny(img,125,175)
cv.imshow('Edge Cascade',canny)

#Dilating the image
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated',dilated)

# Eroding
eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)

#Resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resized',resized)

#Cropping
cropped=img[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)
