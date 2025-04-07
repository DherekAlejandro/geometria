from cgitb import text
from cmath import atan, cos, sin, sqrt, tan
from distutils import text_file
import math
from pickle import TRUE
from tkinter import E, N, Y, Menu
pi=3.141592653

def LMG_DIRECTO1():
    print("ESTE ES EL CALCULO DE LONGITUDE MEDIA DE GAUSS METODO DIRECTO\n ES DECIR, CONOCIDOS UNA DISTANCIA GEODESICA ENTRE A Y B, LAS CORRDENADAS DE A Y EL AZIMUT DE A-B ")
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
      
    AS=input("¿coordenadas en decimal?")
    if AS=="si":
        latitudAt=float(input("Ingrese Latitud de A en decimal:\n"))
        longitudAt=float(input("Ingrese longitud de A en decimal:\n"))
    else:
        latitudAg=(float(input("Ingrese los grados de la latitud de A:\n")))    
        latitudAm=(float(input("Ingrese los minutos de la latitud de A:\n")))
        latitudAs=(float(input("Ingrese los segundos de la latitud de A:\n")))
        if latitudAg<0:
            latitudAt=latitudAg-(latitudAm/60)-(latitudAs/3600)
        else:
            latitudAt=latitudAg+(latitudAm/60)+(latitudAs/3600)    
        longitudAg=(float(input("Ingrese los grados de la longitud de A:\n")))    
        longitudAm=(float(input("Ingrese los minutos de la longitud de A:\n")))
        longitudAs=(float(input("Ingrese los segundos de la longitud de A:\n")))        
        if longitudAg<0:
            longitudAt=longitudAg-(longitudAm/60)-(longitudAs/3600)
        else:    
            longitudAt=longitudAg+(longitudAm/60)+(longitudAs/3600)
    Sgeo=float(input("Ingrese la distancia geodesica entre A Y B(S):\n"))
    azi=float(input("Ingrese Azimut en grados:\n")) 
    azig=float(input("Ingrese los grados del Azimut:\n"))
    azim=float(input("Ingrese los minutos del Azimut:\n"))
    azis=float(input("Ingrese los segundos del Azimut:\n"))
    if azig<0:
        AziT=azig-(azim/60)-(azis/3600)
    else:
        AziT=azig+(azim/60)+(azis/3600)
    #calculos
    F=float(1/f)
    E=float((2*F - pow(F,2)))
    e2=float(E)
    p1=sqrt(1-e2*pow(sin(math.radians(latitudAt)),2))
    p2=sqrt(pow(1-e2*pow(sin(math.radians(latitudAt)),2),3))
    N1=(a/p1)
    M1=(a(1-e2)/p2)
    #aproximacion del punto
    delati= Sgeo*cos(math.radians(AziT))/M1
    delongi=Sgeo*sin(math.radians(AziT))/(N1*cos(math.radians(latitudAt)))
    LatitudBT=latitudAt + delati
    longitudBT=longitudAt + delongi
    #calculo del exacto del punto con latitud, longitud y azimut
    latitud=(latitudAt+LatitudBT)/2
    t=tan(math.radians(latitud))
    n2=(e2/(1-e2))*pow(cos(math.radians(latitud)),2)
    v2=(1*+n2)
    deltaazimut=delongi*((1+n2)/12)*(pow(delongi*pow(cos(math.radians(latitud))),2)) + ((3+8*n2)*pow(delongi,2)/24*v2*v2)
    Azimut=AziT+ deltaazimut/2
    deltalatitud=(1/M1)*(Sgeo*cos(math.radians(Azimut)/cos(delongi/2)))*(1-((1-2*n2)*(delongi)/24))
    deltalongitud=(1/N1)*(Sgeo*sin(math.radians(Azimut))/cos(latitud))*(1+(delongi*pow(sin(math.radians(latitud)),2)/24)-(1+n2-9*n2*t*t)*(pow(delati,2))/(24*v2*v2))