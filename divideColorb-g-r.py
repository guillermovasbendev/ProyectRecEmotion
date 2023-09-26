import cv2 as cv
import matplotlib.pyplot as plt

# Lee la imagen de entrada desde el archivo "smiley.jpg"
img = cv.imread("images/smiley.jpg")

# Muestra la imagen original utilizando OpenCV
cv.imshow("imagen", img)

# Divide la imagen en sus canales de color: azul (B), verde (G) y rojo (R)
b, g, r = cv.split(img)

# Muestra cada canal de color por separado utilizando OpenCV
cv.imshow("blue", b)
cv.imshow("green", g)
cv.imshow("red", r)

# Imprime las dimensiones de la imagen original y de cada canal de color
print("Dimensiones de la imagen original:", img.shape)
print("Dimensiones del canal azul (B):", b.shape)
print("Dimensiones del canal verde (G):", g.shape)
print("Dimensiones del canal rojo (R):", r.shape)

# Espera hasta que se presione una tecla (0 significa que esperará indefinidamente)
cv.waitKey(0)

# Cierra todas las ventanas de imagen abiertas por OpenCV
cv.destroyAllWindows()
