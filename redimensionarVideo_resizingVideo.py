# the first part of the code defines a function to change the size
import cv2 as cv



def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# the second part of the code captures and displays the frames

capture = cv.VideoCapture("videos/robot.mp4")
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=.2)
    # its posible change the size add how parameter of before line
   # frame_resized = rescaleFrame(frame, scale=.2) and change de number for minus scale
    cv.imshow("video", frame)
    cv.imshow("video Resized", frame_resized)

    if cv.waitKey(150) & 0xFF == ord("d"):#its posible change time of close the window, for the operative system believe the window not send answer
        break

    # Check if the user clicked the close button on any of the windows
    if cv.getWindowProperty("video", cv.WND_PROP_VISIBLE) < 1 or cv.getWindowProperty("video Resized", cv.WND_PROP_VISIBLE) < 1:
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)

# Note: Resizing the frames can affect the speed of the video,
# as it requires additional processing time. The larger the video and
# the more intensive the resizing, the greater the impact on speed. The
# performance can also be influenced by the capabilities of the computer's
# processor, as a faster processor with more cores can handle resizing
# more efficiently, resulting in faster and smoother video playback.