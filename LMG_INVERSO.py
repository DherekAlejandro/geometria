from cgitb import text
from cmath import atan, cos, sin, sqrt, tan
from distutils import text_file
import math
from pickle import TRUE
from tkinter import E, N, Y, Menu
pi=3.141592653
def LMG_PROBLEMA_INVERSO():
    ws=input("¿Trabajamos con el sistema de coordenadas WGS-84?\n")
    if ws=="si" or ws=="SI":
            f=297
            a=6378388
    else:    
        f=float(input("ingrese f:\n"))
        A1=input("¿el valor de a es:6´378.388?\n")
        if A1=="si":
            a=6378388
            print(" ¡Genial! es el valor con el que estamos trabajando")
        else: 
            a=float(input("ingrese a"))
    F=float(1/f)
    E=float((2 *F  - pow(F,2)))
    e2=float(E)
    deci=input("¿Grados decimales?\n")
    if deci=="si":
        y1=float(math.radians(input("ingrese la latitud punto 1 en decimal\n")))
        l1=float(math.radians(input("ingrese la Longitud punto 1 en decimal\n")))
        y2=float(math.radians(input("ingrese la latitud punto 2 en decimal\n")))
        l2=float(math.radians(input("ingrese la Longitud punto 2 en decimal\n")))
    else:
        #l1
        print("ingrese la Longitud punto 1 en grados\n")
        Gral1= float(input("ingrese los grados de la Longitud 1\n"))
        minl1= float(input("ingrese los minutos de la Longitud 1\n"))
        segl1= float(input("ingrese los segundos de la Longitud 1\n"))
        if Gral1<0:
            l1=float(Gral1-(minl1/60)-(segl1/3600))
        else:
            l1=float(Gral1+(minl1/60)+(segl1/3600))
        #y1
        print("ingrese la Latitud punto 1 en grados\n")
        Gra= float(input("ingrese los grados de la Latitud 1\n"))
        min= float(input("ingrese los minutos de la Latitud 1\n"))
        seg= float(input("ingrese los segundos de la Latitud 1\n"))
        if Gra<0:
            y1=float(Gra-(min/60)-(seg/3600))
        else:
            y1=float(Gra+(min/60)+(seg/3600))
        #l2
        print("ingrese la Longitud punto 2 en grados\n")
        Gral2= float(input("ingrese los grados de la Longitud 2\n"))
        minl2= float(input("ingrese los minutos de la Longitud 2\n"))
        segl2= float(input("ingrese los segundos de la Longitud 2\n"))
        if Gral2<0:
            l2=float(Gral2-(minl2/60)-(segl2/3600))
        else:
            l2=float(Gral2+(minl2/60)+(segl2/3600))
        #y2
        print("ingrese la Latitud punto 2 en grados\n")
        Gra2= float(input("ingrese los grados de la Latitud 2\n"))
        min2= float(input("ingrese los minutos de la Latitud 2\n"))
        seg2= float(input("ingrese los segundos de la Latitud 2\n"))
        if Gra2<0:
            y2=float(Gra2-(min2/60)-(seg2/3600))
        else:
            y2=float(Gra2+(min2/60)+(seg2/3600))
    ##calculo de constantes
    diy=y2-y1
    dil=float((l2-l1))
    y=float(((y1 + y2)/2)) 
    t= math.tan(y)
    n2=( e2 /1-e2) * pow(cos(y),2)
    v2= 1+n2
    p=sqrt((1-e2 * pow(sin(y),2)))
    p1=sqrt((1-e2 * pow(sin(y),2))) * (1-e2*pow(sin(y),2))
    N=((a/p))
    M=((a * (1-e2)/p1))
    #calculo de azimutes 
    B=float(N * dil * cos(y) * (1 - ((1/24) * pow(dil * sin(Y)),2)+((pow(diy,2)) * (1 + n2 - 9 * n2 * pow(t,2)))/(24 * pow(v2,2))))
    A=float((M * diy * cos(dil/2) * (1 +  (pow(diy*cos(y),2))*((1-  2 * n2)/24) +(n2 * (1-  pow(t,2)) * (pow(diy,2))/(B * pow(v2,2))))))
    ## distancia geodesica
    S=float(sqrt(pow(A,2)+pow(B,2)))
    ##azimute total
    az=atan(B/A)
    difaz= dil * sin(y) * (1 + ((1 + n2)/ 12) * (pow(dil*cos(y),2))+((3+8*n2)/24*pow(v2,2))*(pow(diy,2)))
    az1=az-(difaz/2)
    az2=az+(difaz/2)
    print("Azimut 1-2:  ",math.degrees(az1),"\nAzimut 2-1:  ",math.degrees(az2), "\ndistancia geodésica(m):  ",S)