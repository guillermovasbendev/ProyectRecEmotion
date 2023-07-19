# blur es desenfocar la imagen esto se hace para eliminar ruido
import cv2 as cv

img =cv.imread("images/smiley.jpg")
# cv.imshow("smile", img)
#la linea anterior solo dibuja la imagen original por eso esta comentada
cv.waitKey(0)

#funcion para convertir la imagen a un difuminado
blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)

cv.imshow("desenfoque", blur)

cv.waitKey(0)
