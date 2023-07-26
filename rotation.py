import cv2 as cv
import numpy as np

img = cv.imread("images/smiley.jpg")

cv.imshow("Smiley", img)

# rotation permite establecer un punto de la matriz como eje de rotacion
def rotation(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

# Llamar a la función de rotación y mostrar la imagen rotada
rotated = rotation(img, 45)
cv.imshow("rotated", rotated)
cv.waitKey(0)
