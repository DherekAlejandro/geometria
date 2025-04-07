from cgitb import text
from cmath import atan, cos, sin, sqrt, tan
from distutils import text_file
import math
from pickle import TRUE
from tkinter import E, N, Y, Menu
from FUNCUONES_TRISECION import  DMS_DD, ctg

#ingreso de datos 
pi = 3.14159265358979323826433832795028841971

def Convertir_grados_decimales():
    Decimales=float(input("ingrese el angulo en decimal:\n"))  
    if Decimales<0:
        grados=float(math.trunc(Decimales))
        minutos=float(60*(Decimales - grados))
        segundos=float(((minutos-math.trunc(minutos))*60))
        print("Grados en sexagecimal")
        print("Grados: ",grados,"Minutos: ",math.trunc(-minutos),"Segundos: ",-segundos)
    else:
        grados=float(math.trunc(Decimales))
        minutos=float(60*(Decimales - grados))
        segundos=float(((minutos-math.trunc(minutos))*60))
        print("Grados en sexagecimal")
        print("Grados: ",grados,"Minutos: ",math.trunc(minutos),"Segundos: ",segundos)

def Convertir_grados_a_decimal():
    Decimales1=input("¿Angulo positivo?:\n")
    if Decimales1=="no":
        grados1=input("ingrese los grados:\n")
        minutos1=input("ingrese los minutos:\n")
        segundos1=input("ingrese los segundos:\n")
        fin=(grados1-(minutos1/60)-(segundos1/3600))
        print("Angulo en decimal es:", fin)
    else:
        grados1=input("ingrese los grados:\n")
        minutos1=input("ingrese los minutos:\n")
        segundos1=input("ingrese los segundos:\n")  
        fin=(grados1+(minutos1/60)+(segundos1/3600))              
        print("Angulo en decimal es:", fin)       
            
def DMS(nombre):
    print(f"Digite grados,minutos y segundos de {nombre} ")
    Grados = float(input("Grados: "))
    Minutos= float(input("Minutos: "))
    Segundos= float(input("Segundos: "))
    return DMS_DD(Grados, Minutos, Segundos)

def CoordenadasP(EA,NA,EB,NB,alfa,beta):
    EP = ((NA-NB)+(EA*ctg(beta))+(EB*ctg(alfa)))/(ctg(beta)+ctg(alfa))
    NP = ((EB-EA)+(NA*ctg(beta))+(NB*ctg(alfa)))/(ctg(beta)+ctg(alfa))
    return EP,NP  