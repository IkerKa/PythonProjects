#Inteligencia que dados unos numeros hechos a mano, los reconozca y los vaya arrastrando
# a la caja de numeros que le corresponde sean un 5 o un 3

#Vamos a hacer un reconocimiento de numeros

import pyautogui
import time
import pyperclip


#Alt + tab
pyautogui.hotkey('alt', 'tab')

time.sleep(2)

#1.---->Reconocimiento de pantalla<---
#captura de pantalla
pyautogui.screenshot('MiroPhotos/pantalla.jpg')




#Entonces ahora haremos el reconocimiento

#El reconocimiento tratará de:
#1.---->Tomar una caja y analizarla
#2.---->Si es un 5 entonces lo arrastrará a la caja de 5 y se repetirá el proceso con menos confianza
#3.---->Si es un 3 entonces lo arrastrará a la caja de 3 y se repetirá el proceso con menos confianza
#4.---->En  caso de que no sea ninguna, se bajará la confianza y se volverá a intentar

#Funcion de reconocimiento que se llamará cada vez que se quiera reconocer un numero
#Tendrá como parámetros la confianza de los 5, los 3 y la imagen de la pantalla
def reconocimiento(confianza5, confianza3, imagen):
    #1. reconocer la zona de numeros
    #2. reconocer el numero que hay dentro
    #3. arrastrar el numero a la caja que le corresponde

    #Localizamos las cajas donde irán los numeros
    caja5 = pyautogui.locateOnScreen('MiroPhotos/cajadecinco.jpg', confidence=0.5)
    caja3 = pyautogui.locateOnScreen('MiroPhotos/cajadetres.jpg', confidence=0.5)

    
    cajaNums = pyautogui.locateOnScreen('MiroPhotos/numerajos_all.jpg', confidence=imagen)
    #Si no encuentra la zona de numeros, entonces no hará nada
    if cajaNums == None:
        #Sonido y mensaje de error
        print('No se ha encontrado la zona de numeros')
        return
    else:
        #Si encuentra la zona desplazamos el raton a ella
        pyautogui.moveTo(cajaNums)

        #Doble busqueda para más precision
        cajaNumsFinal = pyautogui.locateOnScreen('MiroPhotos/numerajos_focus.jpg', confidence=imagen)
        #Si no encuentra la zona de numeros, entonces no hará nada
        if cajaNumsFinal == None:
            #Sonido y mensaje de error
            print('No se ha encontrado la zona de numeros')
            return
        else:

            pyautogui.moveTo(cajaNumsFinal)
            #Ahora vamos a buscar en esa zona los diferentes numeros
            #1.---->Nos movemos a un numero
            #2.---->Lo arrastramos a la caja

            num5 = pyautogui.locateOnScreen('MiroPhotos/5definitivo.jpg', confidence=confianza5)
            num3 = pyautogui.locateOnScreen('MiroPhotos/3definitivo.jpg', confidence=confianza3)

            print(num5)
            print(num3)

            #Ahora compararemos si es un 5 o un 3
            if num5 != None:

                #Si es un 5, lo comprobamos mas a fondo
                pyautogui.moveTo(num5)
                num5Final = pyautogui.locateOnScreen('MiroPhotos/esUnCinco.jpg', confidence=0.20)

                print(num5Final)

                if num5Final != None:
                    #Si es un 5, lo arrastramos a la caja de 5
                    pyautogui.moveTo(num5)
                    pyautogui.mouseDown()
                    pyautogui.moveTo(caja5)
                    pyautogui.mouseUp()
                    #Sonido y mensaje de que ha encontrado un 5
                    print('Se ha encontrado un 5')
                    return
                else:
                    #Si no es un 5, no hacemos nadaç
                    pyautogui.moveTo(num3)
                    pyautogui.mouseDown()
                    pyautogui.moveTo(caja3)
                    pyautogui.mouseUp()
                    #Sonido y mensaje de que ha encontrado un 3
                    print('Se ha encontrado un 3')
                    return

            
            elif num3 != None:
                    
                #Si es un 3, lo comprobamos mas a fondo
                pyautogui.moveTo(num3)
                num3Final = pyautogui.locateOnScreen('MiroPhotos/esUnTres.jpg', confidence=0.20)

                if num3Final != None:
                    #Si es un 3, lo arrastramos a la caja de 3
                    pyautogui.moveTo(num3)
                    pyautogui.mouseDown()
                    pyautogui.moveTo(caja3)
                    pyautogui.mouseUp()
                    #Sonido y mensaje de que ha encontrado un 3
                    print('Se ha encontrado un 3')
                    return
                else:
                    #Si no es un 3, bajamos la confianza
                    pyautogui.moveTo(num5)
                    pyautogui.mouseDown()
                    pyautogui.moveTo(caja5)
                    pyautogui.mouseUp()
                    #Sonido y mensaje de que ha encontrado un 5
                    print('Se ha encontrado un 5')
                    return
            else:
                #Si no es ninguno, bajamos la confianza
                print('No es ninguno')
                return


#MAIN   
#Vamos a hacer un bucle infinito que cada 5 segundos reconozca la pantalla
confianza5 = 0.8
confianza3 = 0.8
imagen = 0.9
for i in range(12):
    reconocimiento(confianza5, confianza3, imagen)
    time.sleep(3)
    #Bajamos la confianza de los numeros
    imagen = imagen - 0.1



