#Este programa abrira la aplicación de "paint" y haga algunos dibujos


import pyautogui
import time
import pyperclip
import pywhatkit as kit


#Abrir paint

pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('mspaint')
time.sleep(1)
pyautogui.press('enter')

#Ahora vamos a dibujar un cuadrado de color rojo

#1.---->Reconocimiento de pantalla<---
#Captura de pantalla
time.sleep(5)
pyautogui.screenshot('captura.png')



#2.---->Reconocimiento de tipo de escritura<---
#Entonces ahora comenzamos la busqueda primero del lapiz con el que escribir

#movemos el raton a la parte superior
pyautogui.moveTo(100, 100, duration=1)


interface = pyautogui.locateOnScreen('paint.jpg', confidence=0.5)

#Movemos el raton a la posicion del lapiz
pyautogui.moveTo(interface)

# Hacemos una búsqueda mas precisa del lapiz
interface2 = pyautogui.locateOnScreen('paint2.jpg', confidence=0.9)

#Movemos el raton a la posicion del lapiz
pyautogui.moveTo(interface2)

#Hacemos click en el lapiz
pyautogui.click(interface2)

time.sleep(5)

#Buscamos el lapiz con el que se quiere dibujar
interface3 = pyautogui.locateOnScreen('lapiz.jpg', confidence=0.9)

pyautogui.moveTo(interface3)
time.sleep(5)
#doble click en el lapiz
pyautogui.doubleClick(interface3)

#3.---->Reconocimiento de grosores de lapiz<---

#Volvemos a colocar el raton arriba
pyautogui.moveTo(100, 100, duration=1)

interface = pyautogui.locateOnScreen('tamano.jpg', confidence=0.9)

#Movemos el raton a la posicion del lapiz
pyautogui.moveTo(interface)

# Hacemos una búsqueda mas precisa del lapiz
interface2 = pyautogui.locateOnScreen('tamano2.jpg', confidence=0.9)

#Movemos el raton a la posicion del lapiz
pyautogui.moveTo(interface2)

#Hacemos click en el lapiz
pyautogui.click(interface2)

time.sleep(5)

#Buscamos el grosor del lapiz
interface3 = pyautogui.locateOnScreen('biengorda.jpg', confidence=0.9)

pyautogui.moveTo(interface3)
time.sleep(5)
#doble click en el grosor
pyautogui.doubleClick(interface3)

#4.---->Reconocimiento de colores<---

#Volvemos a colocar el raton arriba
pyautogui.moveTo(100, 100, duration=1)

interface = pyautogui.locateOnScreen('colors.jpg', confidence=0.9)

#Movemos el raton a la posicion del lapiz
pyautogui.moveTo(interface)

# Hacemos una búsqueda mas precisa del color
interface2 = pyautogui.locateOnScreen('colors2.jpg', confidence=0.9)

#Movemos el raton a la posicion del color
pyautogui.moveTo(interface2)

#Hacemos click en el color
pyautogui.click(interface2)

time.sleep(5)

#centramos el raton en la pantalla
pyautogui.moveTo(400, 400, duration=1)


#4.---->Reconocimiento Cuadrado<---

#Vamos a dibujar un cuadrado

pyautogui.dragTo(500, 400, button='left')
pyautogui.dragTo(500,300, button='left')
pyautogui.dragTo(400, 300, button='left')
pyautogui.dragTo(400, 400, button='left')


#5.---->Reconocimiento de relleno<---

#Volvemos a colocar el raton arriba
pyautogui.moveTo(100, 100, duration=1)

interface = pyautogui.locateOnScreen('tuls.jpg', confidence=0.9)
pyautogui.moveTo(interface)

time.sleep(5)
interface2 = pyautogui.locateOnScreen('tuls2.jpg', confidence=0.9)
pyautogui.moveTo(interface2)
pyautogui.click(interface2)

time.sleep(5)

#Buscamos el relleno
interface3 = pyautogui.locateOnScreen('colors.jpg', confidence=0.9)
pyautogui.moveTo(interface3)
interface = pyautogui.locateOnScreen('colors3.jpg', confidence=0.9)
pyautogui.moveTo(interface)
pyautogui.click(interface)

time.sleep(5)


#Hacemos click en el cuadrado
pyautogui.click(450,350, button='left')


#6.---->Escritura de palabras<---

#Volvemos a colocar el raton arriba
pyautogui.moveTo(100, 100, duration=1)

interface = pyautogui.locateOnScreen('tuls.jpg', confidence=0.9)
pyautogui.moveTo(interface)
interface2 = pyautogui.locateOnScreen('tuls4.jpg', confidence=0.9)
pyautogui.moveTo(interface2)
pyautogui.click(interface2)

time.sleep(5)

#Hacemos click encima del cuadrado
pyautogui.click(300,350, button='left')

#Escribimos la palabra
pyautogui.write('CONIO VERDE', interval=0.25)

#7.---->Reconocimiento de envio<---

#Volvemos a colocar el raton arriba y hacemos una captura de pantalla
pyautogui.moveTo(100, 100, duration=1)
pyautogui.screenshot('captura2.jpg')

#8.----->Envio de foto por whatsapp<---

# Coming Soon...

# #Tenemos que buscar el visual

# interface = pyautogui.locateOnScreen('navbar.jpg', confidence=0.9)
# pyautogui.moveTo(interface)
# interface2 = pyautogui.locateOnScreen('vscode.jpg', confidence=0.9)
# pyautogui.moveTo(interface2)

# time.sleep(5)

# #Hacemos click en el visual
# pyautogui.click(interface2)

# time.sleep(5)

# #Buscamos el path
# interface3 = pyautogui.locateOnScreen('path.jpg', confidence=0.9)
# pyautogui.moveTo(interface3)
# interface4 = pyautogui.locateOnScreen('path2.jpg', confidence=0.9)

# time.sleep(5)

# #Hacemos click en el path
# pyautogui.click(interface4)

# #Combinacion de teclas Shift + Alt + C nos guardamos en el porta papeles el path
# pyautogui.hotkey('shift', 'alt', 'c')

# # time.sleep(5)

# # pyautogui.hotkey('win', 'r')
# path = pyperclip.paste()
# # pyautogui.write(path, interval=0.25)
# # pyautogui.press('enter')

# # time.sleep(8)

# #Enviamos por whatsapp el path
# kit.sendwhats_image("+34 686 47 56 61",path,"Mira que bonito cuadrado")












