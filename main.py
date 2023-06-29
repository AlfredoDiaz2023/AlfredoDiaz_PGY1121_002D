from Libreria import *
import numpy as np
import random as rn
####################################



#####################################
def ingresarLibreria(arreglo_libreria):
    libro = libreria()
ciclo = True
while ciclo:
    print("Menu Libreria")
    print("1) Ingrese Libro")
    print("2) Buscar Libro")
    print("3) Informe del Libro")
    print("4) Salir")
    op = int(input("Seleccione 1-4:"))
    try:
        match op:
            case 1:
                arreglo_libreria = arreglo_libreria(arreglo_libreria)
            case 2:
                arreglo_libreria = arreglo_libreria(arreglo_libreria)
            case 3:
                arreglo_libreria = arreglo_libreria(arreglo_libreria)
            case 4:
                print("Salir")
                print("Gracias por preferirnos Alfredo Diaz V.1")

    except BaseException as error:
        print(f"Error:{error}")
