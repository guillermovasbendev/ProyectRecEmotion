import cv2 as cv

def rescaleImage(image, scale=0.75):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(image, dimensions, interpolation=cv.INTER_AREA)

image = cv.imread("images/smiley.jpg")
image_resized = rescaleImage(image, scale=0.5)

cv.imshow("Image", image)
cv.imshow("Resized Image", image_resized)

cv.waitKey(0)
cv.destroyAllWindows()
