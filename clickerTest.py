#Script para clickar un + en una pestaña web

import pyautogui
from PIL import Image
import time
import cv2

#Reconocer un btoon verde en la pantalla de color #28a745

#hacemos una captura de la pestaña
time.sleep(5)
captura = pyautogui.screenshot(region=(0,0, 1920, 1080))

captura.save('captura.png')

#buscamos el boton verde
imagen = Image.open('captura.png')

#buscamos el boton verde
posicion = pyautogui.locateOnScreen('sax.jpg', confidence=0.9)

print(posicion)

#movemos el raton a la posicion del boton
pyautogui.moveTo(posicion)
pyautogui.click()
#scroll
# pyautogui.scroll(-1000000)

#Escribe hola
pyautogui.typewrite('Hola que tal no soy iker soy python')

# #Pulsa enter
pyautogui.press('enter')

#clickamos el boton muchas veces
