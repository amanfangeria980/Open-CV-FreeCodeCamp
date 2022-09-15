# Drawing Shapes and Putting Texts 
import this
import cv2 as cv
import numpy as np

# Blank image
blank=np.zeros((500,500,3),'uint8')
cv.imshow('Blank Window',blank)

img = cv.imread('Resources/Photos/cat.jpg')

cv.imshow('Image Window',img)

# 1.Paint the image a certain colour
blank[:]=0,255,0
blank[200:300,300:400]=0,0,255
cv.imshow('Green Window',blank)

# 2.Draw a Rectangle
cv.rectangle(blank,(0,0),(200,200),(255,0,0),thickness=2)
# thickness=CV.FILLED will fill the whole rectangle or -1 does the same thing
cv.imshow('Rect 1',blank)
# we can also do this
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness=2)
cv.imshow('Rect 1',blank)


# 3.Draw a Cicle
cv.circle(blank,(250,250),55,(255,0,0),thickness=3)
cv.imshow('circle',blank)

# 4.Draw a Line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness=2)
cv.imshow('Line',blank)

# 5.Write Text
cv.putText(blank,'Hello',(250,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),2)
cv.imshow('Text',blank)
cv.waitKey(0)