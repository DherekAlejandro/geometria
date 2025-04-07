from cgitb import text
from cmath import atan, cos, sin, sqrt, tan
from distutils import text_file
import math
from pickle import TRUE
from tkinter import E, N, Y, Menu


def biseccion():
    print("METODO DE CALCULO DE Np Y Ep CON COORDENADAS Na,Ea,Nb,Eb")
    #este seria igual al Na
    Na=float(input(("Ingrese la coordenada Norte de A:\n")))
    #este seria igual al Ea
    Ea=float(input(("Ingrese la coordenada Este de A:\n")))
    #este seria igual al Nb
    Nb=float(input(("Ingrese la coordenada Norte de B:\n")))
    #eset seria igual a Eb
    Eb=float(input(("Ingrese la coordenada Este de B:\n")))
    As=input(("¿Alpha en grados en decimales?\n"))
    if As=="si":
        AlphaT=float(input("ingrese Alpha en decimal:\n"))
    else:
        Alphag=float(input(("ingrese grados de Alpha:\n")))
        Alpham=float(input(("ingrese minutos de Alpha:\n")))
        Alphas=float(input(("ingrese segundos de Alpha:\n")))
        AlphaT=float(Alphag+(Alpham/60)+(Alphas/3600))
        
    Bs=input(("¿Beta en grados en decimales?\n"))
    if Bs=="si":
        BetaT=float(input("ingrese Beta en decimal\n"))
    else:
        Betag=float(input(("ingrese grados de Beta\n")))
        Betam=float(input(("ingrese minutos de Beta\n")))
        Betas=float(input(("ingrese segundos de Beta\n")))
        BetaT=float(Betag+(Betam/60)+(Betas/3600))
    DE=Ea-Eb
    DN=Na-Nb    
    ctgB=1/tan(math.radians(BetaT))
    ctgA=1/tan(math.radians(AlphaT))
    Np=(DE + Na*(ctgB) + Nb*(ctgA))/(ctgA + ctgB)
    Ep=(DN + Ea*(ctgB) + Eb*(ctgA))/(ctgA + ctgB)
    print("la coordenada de Np:   ",Np,"\nla coordenada de Ep:   ",Ep)
biseccion()