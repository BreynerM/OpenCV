#Librería
import cv2
import numpy as np
#se crea un array 'bgr' con np.zeros con el tamño indicado iniciado en cero
bgr=np.zeros((300,300,3),dtype=np.uint8) #uint8 es un tipo de dato usado en imagenes (8 bits) que va desde 0 hasta 255.
bgr[:,:,:]=(0,255,255) #se le asigna el color amarillo al array 'bgr' 0, 255, 255 es amarillo en rgb.
cv2.imshow('BGR',bgr) #la funcion imshow sirve para mostrar el array especificado

#funcion para poder cerrar la ventana, el argumento que recibe sirve para saber en milisegundos cuanto tarda en cerrar
cv2.waitKey(0) 
cv2.destroyAllWindows() #funcion para cerrar todo el proceso.