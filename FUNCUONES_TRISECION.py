from cgitb import text
from cmath import atan, cos, sin, sqrt, tan
from distutils import text_file
import math
from pickle import TRUE
from tkinter import E, N, Y, Menu
pi=3.141592653

# From DMS(degrees,minutes,seconds) to DD(Decimal degrees)
def DMS_DD(Grados,Minutos,Segundos):
    resultado = Grados + (Minutos/60) + (Segundos/3600)
    return resultado
# From DD(Decimal degrees) to DMS(degrees,minutes,seconds)
def DD_DMS(Valor_Sexadecimal):

    Grados = int(Valor_Sexadecimal)
    Minutos = int(((Valor_Sexadecimal-Grados)*60))
    Segundos = ((Valor_Sexadecimal-Grados-(Minutos/60))*3600)

    if Valor_Sexadecimal<0:
        Minutos=-Minutos
        Segundos=-Segundos
    return "{}°{}''{}'".format(Grados,Minutos,Segundos)    
def Coordenadas(Nombre):
    Este = float(input(f"\nDigite la coordenada este de la estacion {Nombre}: "))
    Norte = float(input(f"Digite la coordenada norte de la estacion {Nombre}: "))
    return Este,Norte

def Direcciones_Horizontales(Nombre):
    A = float(input(f"Digite la direccion horizontal {Nombre} (Grados): "))
    B = float(input(f"Digite la direccion horizontal {Nombre}  (Minutos): "))
    C = float(input(f"Digite la direccion horizontal {Nombre}  (Segundos): "))
    return DMS_DD(A,B,C)

# Determinación de angulos ABC 

def AngulosABC(EA,NA,EB,NB,EC,NC):

    A = math.degrees((math.atan((EC-EA)/(NC-NA)))-(math.atan((EB-EA)/(NB-NA))))
    B = math.degrees((math.atan((EA-EB)/(NA-NB)))-(math.atan((EC-EB)/(NC-NB))))
    C = math.degrees((math.atan((EB-EC)/(NB-NC)))-(math.atan((EA-EC)/(NA-NC))))

    if A<0:
        A+=180
    elif B<0:
        B+=180
    elif C<0:
        C+=180        
    
    return A,B,C

def ctg(degrees):
    resultado = 1/(math.tan(degrees))
    return resultado    

def ConstantesK(A,x,B,y,C,z):
    K1 = 1 / (ctg(A)-ctg(x))
    K2 = 1 / (ctg(B)-ctg(y))
    K3 = 1 / (ctg(C)-ctg(z))
    return K1,K2,K3

# Coordenadas de P-Trisección

def CoordenadasP(EA,EB,EC,NA,NB,NC,K1,K2,K3):
    EP=((K1*EA)+(K2*EB)+(K3*EC))/(K1+K2+K3)
    NP=((K1*NA)+(K2*NB)+(K3*NC))/(K1+K2+K3)
    return EP,NP