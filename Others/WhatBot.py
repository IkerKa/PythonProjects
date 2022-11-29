#Plantilla para enviar mensajes a un número de whatsapp

import pyautogui
import time
import pyperclip

#Ponemos el numero de telefono
numero = '34666666666'

#Ponemos el mensaje
mensaje = 'Chueck this out'


#Buscamos el whatsapp web
interface = pyautogui.locateOnScreen('whatsapp.jpg', confidence=0.9)