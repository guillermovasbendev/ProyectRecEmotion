# this is a example how read a video with the library  openCV
import cv2 as cv

capture =cv.VideoCapture("videos/robot.mp4")#0,1,2 o r 3 for cameras 
while True: #make a infinite bucle while succes some condition
    isTrue, frame=capture.read()
    cv.imshow("video",frame)#capture the frame

    if cv.waitKey(20) & 0xFF==ord("d"):#wait for 20ms to press the key
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)

# in the line four its parameters can be numbers 0,1,2.etc where 0 is your pc camera for defect, 1 the second camera and 2 your third camera
# 
#  or  can use a route relative for example c/video/robot.mp4