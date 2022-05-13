from random import choice
from utiles import *


def adivinar(): #elige una palabra al azar
    LISTA = ["abran", "besos", "espia", "gatos", "manda"]
    palabra = choice(LISTA)
    return palabra

def palabra_arriesgo (): #Recibe una palabra al azar y devuelve un booleano si se adivina mientras sea de len 5 
    PALABRA = adivinar()
    adivinar_1 = print("Palabra a adivinar: ?????")
    arriesgo = input("Arriesgo: ")
    ganaste = False
    while len(arriesgo) != 5:
        print ("El largo de la palabra debe contener 5 letras\n")
        arriesgo = input("Arriesgo: \n")

    for i in range (0, len(arriesgo)):

        if i in range (0, len (PALABRA)):

            if arriesgo[i] == PALABRA[i]:
                print (obtener_color("Verde") + arriesgo[i], end = "")

            elif (arriesgo[i] in PALABRA) and arriesgo[i] != PALABRA[i]:
                print (obtener_color("Amarillo") + arriesgo[i], end = "")

            else:
                print (obtener_color("Defecto") + arriesgo[i], end = "")

    if arriesgo == PALABRA:
        adivinar_1 = print(obtener_color("Defecto") + "\nPalabra a adivinar: ", PALABRA)
        print("Ganaste!")
        #ganaste = True 
    else:
        adivinar_1 = print(obtener_color("Defecto") + "\nPalabra a adivinar: ", PALABRA)
        print("Perdiste!")
        #ganaste = False

    return ganaste

palabra_arriesgo ()