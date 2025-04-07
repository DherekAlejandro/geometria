from ast import If
from cgitb import text
from cmath import atan, cos, sin, sqrt, tan
from distutils import text_file
import math
from pickle import TRUE
from tkinter import E, N, Y, Menu
pi=3.141592653
def TOTAL():

    f=297
    a=6378388        
    F=float(1/f)
    E=float((2*F - pow(F,2)))
    e2=float(E)
    def geodesicas():
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
        N= a/sqrt((1-e2*math.sin(latitud)*math.sin(latitud)))
        Z=N*(1-e2)*sin(latitud)
        X= N*cos(latitud)
        z_x= tan(latitud)*(1-e2) 
            
        print("Coordenada Z: ",Z, "\nCoordenada X: ",X, "\nCoordenada Z/X: ",z_x)
    def geocentricas():
            x=float(input("ingrese x: "))
            z=float(input("ingrese z: "))
            print("ingrese w en grados\n")
            Gra1= float(input("ingrese los grados de w\n"))
            min1= float(input("ingrese los minutos de w\n"))
            seg1= float(input("ingrese los segundos de w\n"))
            if Gra1<0:
                w1=float(Gra1-(min1/60)-(seg1/3600))
            else:
                w1=float(Gra1+(min1/60)+(seg1/3600))
            print( "la latitud es:", w1)
            w=(w1*(pi/180))
            RG=pow((pow(x,2)+ pow(z,2)),0.5)
            Z=RG*sin(w)
            X=RG*cos(w)
            z_x=tan(w)
            print("Coordenada Z: ",Z,"\nCoordenada X: ",X,"\nCoordenada Z/X: ",z_x)
    def parametricas():
            At=input("¿el valor del semieje menores: a=6.378.388?\n")
            if At=="si":
                a=6378388
                f=297
                print(" ¡Genial! es el valor con el que estamos trabajando")
            else: 
                a=float(input("ingrese a"))

            b= (1-F)*a
            print("ingrese tetha en grados\n")
            Gra1= float(input("ingrese los grados de tetha\n"))
            min1= float(input("ingrese los minutos de tetha\n"))
            seg1= float(input("ingrese los segundos de tetha\n"))
            if Gra1<0:
                w1=float(Gra1-(min1/60)-(seg1/3600))
            else:
                w1=float(Gra1+(min1/60)+(seg1/3600))
            print( "la latitud es:", w1)
            w=(w1*(pi/180))        
            Z= b*sin(w)
            X= a*cos(w)
            z_x=(b/a)*tan(w)
            print("Coordenada x= ",X,"\nCoordenada z= ",Z,"\nCoordenadas z/x= ",z_x)

    option="0"
    while not(option=="4"):
        print("MENU DE CALCULO DE LATITUDES DE LA ELIPSE MERIDIANA, ¿QUE DESEA CALCULAR?:")
        print("1.LATITUD GEODESICA")
        print("2.LATITUD GEOCENTRICA")
        print("3.LATITUD PARAMETRICA")
        print("4.SALIR") 
        option= input("SELECIONE DEL 1-4:\n")
        if option=="1":
            geodesicas()
        elif option=="2":
            geocentricas()
        elif option=="3":
            parametricas()
        elif option=="4":
            print("SALIENDO DEL PROGRAMA")    
                           