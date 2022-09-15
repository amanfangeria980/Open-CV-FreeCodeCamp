#Resizing and Rescaling Frames

from ctypes import resize
import cv2 as cv

# Method 1
# This method will work for images,videos and live videos
def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# Method 2 
# It only works for live video
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

img = cv.imread('Resources/Photos/cat.jpg')
resize_img=rescaleFrame(img,0.5)
cv.imshow('Cat Original',img)
cv.imshow('Cat Resized',resize_img)


cv.waitKey(0)



capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue,frame = capture.read()
    resized_frame=rescaleFrame(frame,0.2)
    cv.imshow('Frame Original',frame)
    cv.imshow('Frame Resized',resized_frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
