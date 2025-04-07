from cgitb import text
from cmath import atan, cos, sin, sqrt, tan
from distutils import text_file
import math
from pickle import TRUE
from tkinter import E, N, Y, Menu
import FUNCIONES, PROBLEMA_DIRECTO_COORDENADAS, PROBLEMA_INVERSO_COORD, LMG_INVERSO, BISECCION, TRISECCION, FUNCUONES_TRISECION, LATITUDES, LMG_DIRECTO 
from FUNCIONES import  Convertir_grados_a_decimal, Convertir_grados_decimales
from PROBLEMA_DIRECTO_COORDENADAS import Problema_directo_coordenadas
from PROBLEMA_INVERSO_COORD import Problema_inverso_coordenadas_xyz
from BISECCION import biseccion
from LMG_INVERSO import LMG_PROBLEMA_INVERSO
from TRISECCION import triseccion
from LATITUDES import  TOTAL
from LMG_DIRECTO import LMG_DIRECTO1
#menu de opciones
opcion="0"
while not(opcion=="9"):
    print("BIENVENIDO AL MENU DE CALCULO DE GEODESIA GEOMETRICA")
    print("1. CALCULO DE LATITUDES")
    print("2. CALULO DE COORDENADAS X,Y,Z(PROBLEMA INVERSO DE COORDENADAS)")
    print("3. CALCULO DE COORDENADAS DE LONGITUD, LATITUD Y ALTURA(PROBLEMA DIRECTO DE COORDENADAS)")
    print("4. CONVERTIRDOR DE GRADOS")
    print("5. CALCULO DE Ep Y Np CON BISECCION")
    print("6. CALCULO DE Ep Y Np CON TRISECCION")
    print("7. CALCULO DE LONGITUD MEDIA DE GAUS(PROBLEMA INVERSO) ")
    print("8. CALCULO DE LONGITUD MEDIA DE GAUUS (PROBLEMA DIRECTO)")
    print("9. SALIR")
    opcion=(input("---SELECIONE UNA OPCION(VALIDAS DESDE EL 1 AL 9)\n"))   
    if opcion=="1":
        TOTAL()
    elif opcion=="2":
        Problema_inverso_coordenadas_xyz()    
    elif opcion=="3":
        Problema_directo_coordenadas()
    elif opcion=="4":
        qa=input("¿DE DECIMALES A SEXAGECIMALES?")
        if qa=="si":
            Convertir_grados_a_decimal()
        else:
            Convertir_grados_decimales()
    elif opcion=="5":
        biseccion()
    elif opcion=="6":
        triseccion()
    elif opcion =="7":
        LMG_PROBLEMA_INVERSO()
    elif opcion=="8":
        LMG_DIRECTO1()
    elif opcion=="9":
        print("SALIENDO DEL MENU")        
    else :
        print("OPACION INVALIDA")
Menu()


   
   
   