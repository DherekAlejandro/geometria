from cgitb import text
from cmath import atan, cos, sin, sqrt, tan
from distutils import text_file
import math
from pickle import TRUE
from tkinter import E, N, Y, Menu
pi=3.141592653
def Problema_inverso_coordenadas_xyz():
    print("CALCULO DE COORDENADAS SABIENDO LONGITUD, LATITUD Y ALTURA")
    ws=input("¿Trabajamos con el sistema de coordenadas WGS-84?\n")
    if ws=="si":
        f=297
        a=6378388
    else:    
        f=float(input("ingrese f:\n"))
        A=input("¿el valor de a es:6´378.388?\n")
        if A=="si":
            a=6378388
            print(" ¡Genial! es el valor con el que estamos trabajando")
        else: 
            a=float(input("ingrese a"))
    #ingreso de datos 
    
    long=input("¿la longitud esta en decimal?\n")
    if long=="si":
         fi=float(input("ingrese la longitud en decimal\n"))
    else:
        print("ingrese la longitud en grados\n")
        Gra= float(input("ingrese los grados de la Longitud\n"))
        min= float(input("ingrese los minutos de la Longitud\n"))
        seg= float(input("ingrese los segundos de la Longitud\n"))
        if Gra<0:
            fi=float(Gra-(min/60)-(seg/3600))
        else:
            fi=float(Gra+(min/60)+(seg/3600))

        print( "la longitud es:", fi)
    longitud=(fi*(pi/180))
    lati=input("¿la latitud esta en decimal?\n")
    if lati=="si":
        lada=float(input("ingrese la latitud en decimal\n"))
    else:
        print("ingrese la latitud en grados\n")
        Gra1= float(input("ingrese los grados de la latitud\n"))
        min1= float(input("ingrese los minutos de la latitud\n"))
        seg1= float(input("ingrese los segundos de la latitud\n"))
        if Gra1<0:
            lada=float(Gra1-(min1/60)-(seg1/3600))
        else:
            lada=float(Gra1+(min1/60)+(seg1/3600))
        print( "la latitud es:", lada)
    latitud=(lada*(pi/180))
    h=float(input("ingrese la altura\n"))
    # asignación de variables y calculo
    F=float(1/f)
    E=float((2*F - pow(F,2)))
    e2=float(E)
    print("f es:",F)
    print("e^2 es:",e2)
    #calculo de x,y,z
    N= a/sqrt((1-e2*math.sin(latitud)*math.sin(latitud)))
    X1=(N+h)*math.cos(latitud)*math.cos(longitud)
    y1=(N+h)*math.cos(latitud)*math.sin(longitud)
    Z1=(N*(1 - e2) + h)*math.sin(latitud)
    
    print("\ncordenada x:  ",X1,"\ncoordenada y:  ",y1,"\ncoordenada z:  ",Z1, "\nN es igual a:   ",N)
Problema_inverso_coordenadas_xyz()