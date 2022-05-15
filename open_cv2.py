#Librería
import cv2
from cv2 import imshow

"""import pytesseract
tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'"""

imgText="cafe"
#Lectura de imagen
img= cv2.imread('cafe.png', 0) #se cambia el flag que es predeterminado 1 a 0 para que lo lea en escala de grises
imshow('Imagen Original',img)


cv2.waitKey(0)
cv2.destroyAllWindows()