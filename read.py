# Reading Images and Video

import cv2 as cv

#Reading images

# img = cv.imread('Resources/Photos/cat.jpg')

# cv.imshow('Cat Window',img)

# cv.waitKey(0)

# Reading Videos
# capture = cv.VideoCapture('Resources/Videos/dog.mp4')

# if you are using webcam you can pass 0 here and follow sequentially if any other camera connected to your PC

# while True:
#     isTrue,frame = capture.read()
#     cv.imshow('Frame Windows',frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()