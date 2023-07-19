# this is a example how read a image with the library  openCV
import cv2 as cv

img =cv.imread("images/smiley.jpg")
cv.imshow("smile", img)
cv.waitKey(0)