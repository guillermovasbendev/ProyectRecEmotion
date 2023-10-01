import cv2 as cv

img=cv.imread("images/perro.jpg")
cv.imshow("imagen original", img )

#en el umbral (tresholding) inverso lo que se hace es invertir el valor por encima del punto de referencia seran ceros, y por debajo del punto de referencia seran unos. En el adaptativo lo que hacemos es dejar que el programa decida ese punto de referencia por si mismo, ya que hacerlo de forma manual puede funcionar algunas veces si tenemos suerte, pero otras veces no lo hara

gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# Umbral adaptativo 
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
cv.imshow("Umbral Inverso", adaptive_thresh)
# gray: Este es el primer argumento y representa la imagen en escala de grises en la que se aplicará la umbralización.

# En este codigo se omite el valor umbral, ya que el metodo .adaptativeThreshold, lo calcula de forma automatica

# 255: Este es el tercer argumento y representa el valor máximo que se asignará a los píxeles que superen el valor umbral. En este caso, se establecerá en 255 (blanco).

# v.adaptiveThreshold() : Se usa para establecer de forma automatica el punto de referencia

# cv.ADAPTIVE_THRESH_MEAN_C: Este es el tercer parámetro y especifica el tipo de umbralización adaptativa que se utilizará. cv.ADAPTIVE_THRESH_MEAN_C indica que se utilizará el método de umbralización adaptativa basado en la media. En este método, el valor umbral se calcula como la media de los valores de intensidad en un área local alrededor de cada píxel. Esto significa que el umbral puede variar según las características locales de la imagen.




cv.waitKey(0)