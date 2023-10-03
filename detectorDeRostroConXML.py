import cv2 as cv

img=cv.imread("images/ayo.jpg")
cv.imshow("persona" ,img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("persona en gris", gray)

haar_cascade=cv.CascadeClassifier("haar_face.xml")

# cv.CascadeClassifier: Esta parte del código crea un objeto de la clase CascadeClassifier de OpenCV. Esta clase se utiliza para detectar objetos (en este caso, caras) en una imagen utilizando clasificadores en cascada.

# "haar_face.xml": Esta es la ruta al archivo XML que contiene el clasificador Haar preentrenado para la detección facial. El clasificador Haar es un tipo de clasificador utilizado para detectar características específicas en imágenes. En este caso, "haar_face.xml" contiene las características específicas para detectar caras.

# haar_cascade: Este es el nombre del objeto que has creado. Puedes utilizar este objeto para detectar caras en imágenes utilizando el clasificador Haar cargado desde el archivo XML.

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)

# gray: Esta es la imagen en escala de grises en la que se van a detectar las caras. Antes de pasar la imagen al clasificador, es común convertirla a escala de grises para reducir la complejidad y aumentar la eficiencia del proceso de detección facial.

# scaleFactor=1.1: Este parámetro compensa la reducción de tamaño de la imagen durante el proceso de detección. Una imagen se reduce a un tamaño específico durante la detección facial para que el clasificador pueda detectar objetos de diferentes tamaños. scaleFactor controla cuánto se reduce la imagen en cada escala. Un valor de 1.1 significa que la imagen se reduce en un 10% cada vez que se escala. si fuera 0.01 seria una escala mucho mas pequeña, de menos del 10#

# minNeighbors=3: Este parámetro especifica cuántos vecinos debe tener un área para que se considere una cara. En otras palabras, este valor controla cuántas detecciones cercanas se deben agrupar para considerar que realmente se ha detectado una cara. Un valor más alto conducirá a una detección más fiable pero potencialmente a una detección más lenta y con menos caras detectadas. mas cuadros al rededor de la deteccion si el valor es mas alto a mas cuadros mas precision, a menos cuadros mas probabilidad de error

# La función detectMultiScale devuelve una lista de rectángulos (representados como tuplas de cuatro números: (x, y, ancho, alto)) que delimitan las áreas donde se detectaron las caras en la imagen.



print(f"Numero de caras encontradas ={len(faces_rect)}")

cv.waitKey(0)