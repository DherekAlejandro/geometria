from cgitb import text
from cmath import atan, cos, sin, sqrt, tan
from distutils import text_file
import math
from pickle import TRUE
from tkinter import E, N, Y, Menu

def Problema_directo_coordenadas():
    #ingreso de datos 
        print("ESTE PROGRAMA CALCULA LAS COORDENADAS EN LONGITUD Y LATITUD DADAS UN X,Y,Z")
        ws=input("¿Trabajamos con el sistema de coordenadas WGS-84?\n")
        if ws=="si" or ws=="SI":
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
        x=float(input("Ingrese la coordenada X:\n"))
        y=float(input("Ingrese la coordenada Y:\n"))
        z=float(input("Ingrese la coordenada Z:\n"))
        p=(pow(pow(x,2)+pow(y,2),0.5))
       
        F=float(1/f)
        E=float((2*F - pow(F,2)))
        e2=float(E)
        #calculo de longitud
        lon=y/(x+ p)
        longi=float(2 * math.atan(lon)) 
        longigra=float(longi)
        #calculo de latitud 
        Yo=float((math.atan((z/(p)))) * (1 - e2/(1-e2)))
        N1=(a/pow(1- e2 * pow(math.sin(Yo),2),0.5))
        Y1=(math.atan((z+ e2*N1* math.sin(Yo))/p))
        N2=(a/pow(1- e2 * pow(math.sin(Y1),2),0.5))
        Y2=(math.atan((z+ e2*N2* math.sin(Y1))/p))
        N3=(a/pow(1- e2 * pow(math.sin(Y2),2),0.5))
        Y3=(math.atan((z+ e2*N3* math.sin(Y2))/p))
        N4=(a/pow(1- e2 * pow(math.sin(Y3),2),0.5))
        Y4=(math.atan((z+ e2*N4* math.sin(Y3))/p))
        h= (p/(cos(Y4)))-N4
         ## #longitud en grados minutos y segundos
        ASD=input("¿Longitud y latitud en grados, minutos y segundos?\n")
        if ASD=="si"  or ASD=="SI":
            Decimales=round(math.degrees(longigra),7)
            if Decimales<0:
                grados=float(math.trunc(Decimales))
                minutos=float(60*(Decimales - grados))
                segundos=float(((minutos-math.trunc(minutos))*60))
                print("LONGITUD ES:","Grados: ",grados,"Minutos: ",math.trunc(-minutos),"Segundos: ",-segundos)
            else:
                grados=float(math.trunc(Decimales))
                minutos=float(60*(Decimales - grados))
                segundos=float(((minutos-math.trunc(minutos))*60))
                print("LONGITUD ES:","Grados: ",grados,"Minutos: ",math.trunc(minutos),"Segundos: ",segundos)
            #calculo latitud en grados minutos y segundos
            Decimales1=round(math.degrees(Y4),7)
            if Decimales1<0:
                grados1=float(math.trunc(Decimales1))
                minutos1=float(60*(Decimales1 - grados1))
                segundos1=float(((minutos1-math.trunc(minutos1))*60))
                print("LATITUD ES:","Grados: ",grados1,"Minutos: ",math.trunc(-minutos1),"Segundos: ",-segundos1)
            else:
                grados1=float(math.trunc(Decimales1))
                minutos1=float(60*(Decimales1 - grados1))
                segundos1=float(((minutos1-math.trunc(minutos1))*60))
                print("LATITUD ES:","Grados: ",grados1,"Minutos: ",math.trunc(minutos1),"Segundos: ",segundos1)        
            
        else: 
            print("la longitud en decimal es:   ",math.degrees(longigra),"\nla latitud en decimal es:   ",math.degrees(Y4),"\nla altura es:   ",h, "\nN es igual:  ",N4)  
        print("\nla altura es:   ",h, "\nN es igual:  ",N4)