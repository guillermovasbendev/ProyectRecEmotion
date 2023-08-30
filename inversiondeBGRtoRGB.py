#como BGR es la imagen dada por defecto aveces se hara necesario invertirl por ejemplo matplotlib, usa un sistema RGB, por lo tanto los rojos se vuelven azules y azules rojos

import cv2 as cv
import matplotlib.pyplot as plt

img =cv.imread("images/smiley.jpg")
 #BGR es la forma predeterminada de mostrar la imagen
cv.imshow("smile", img)

# plt.imshow(img)  #RGB es la forma predeterminada de mostrar la imagen en matplotlib
# plt.show()

#de BGR a RGB
rgb=cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)

#las siguientes lineas muestran la imagen invertida en matplotlib
# es decir con los colores correctamente  
plt.imshow(rgb)
plt.show()


cv.waitKey(0)