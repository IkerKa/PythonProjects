#Inteligencia que dados unos numeros hechos a mano, los reconozca y los vaya arrastrando
# a la caja de numeros que le corresponde sean un 5 o un 3

#Vamos a hacer un reconocimiento de numeros

import pyautogui
import time
import pyperclip


time.sleep(2)

#1.---->Reconocimiento de pantalla<---
#captura de pantalla
pyautogui.screenshot('pantalla.jpg')




#Entonces ahora haremos el reconocimiento

#Será un bucle en el que en una foto de la pantalla, dispondremos un conjunto 
#de números donde a partir de dos imagenes buenas de un 3 y un 5, pueda reconocer
#un numero del conjunto y arrastrarlo a la caja de numeros que le corresponde

def recognition_3es():
    #Primero movemos el raton al conjunto de numeros
    interface = pyautogui.locateOnScreen('numerajos', confidence=0.9)

    interface2 = pyautogui.locateOnScreen('cajadetres', confidence=0.9)
    interface3 = pyautogui.locateOnScreen('cajadecinco', confidence=0.9)

    #Entonces a partir de ahi, vamos a hacer un bucle que vaya moviendo el raton
    #a cada uno de los numeros y los vaya comparando con las imagenes de 3 y 5
    #para ver si coincide con alguno de los dos


    #La confidence es la confianza que tiene el programa de que es el numero que
    #estamos buscando, si es muy baja, puede que no lo encuentre, si es muy alta
    #puede que encuentre numeros que no son los que buscamos y nos de error
    elTres = pyautogui.locateOnScreen('3definito.jpg', confidence=0.5)

    #Si encuentra el tres, lo arrastra a la caja de numeros
    if elTres != None:
        pyautogui.moveTo(elTres)
        pyautogui.dragTo(interface2)
    
    #Si no encuentra el tres, busca el cinco
    else:
        elCinco = pyautogui.locateOnScreen('5definito.jpg', confidence=0.5)
        pyautogui.moveTo(elCinco)
        pyautogui.dragTo(interface3)



#Ahora vamos a hacer un reconocimiento de numeros

#Llamamos a la funcion
recognition_3es()
