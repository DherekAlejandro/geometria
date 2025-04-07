import math

import FUNCIONES
import FUNCUONES_TRISECION
from FUNCIONES import DMS


def triseccion():

    def opcion1(AB,AP,BC,BP,CP,CB):
        alfa = AB-AP
        gamma = BC-BP
        fi = 360 -(gamma+theta)
        omega = 180 - (alfa+fi)
        epsilon = CP - CB
        rho = 180 - (epsilon+gamma)

        return omega,rho

    def opcion2():
        alfa = DMS("Alfa(α) ")
        gamma= DMS("Gamma(γ) ")
        epsilon = DMS("Epsilon(ε) ")
        fi = 360 -(gamma+theta)
        omega = 180 - (alfa+fi)
        rho = 180 - (epsilon+gamma)

        return omega,rho

    def datos(beta,theta,eta,omega,rho):

        A= math.radians(beta) 
        B = math.radians(theta)
        C = math.radians(eta) 
        y = math.radians(rho + omega)
        x = math.radians(360 - rho)
        z = math.radians(360 - omega)

        K1,K2,K3 = FUNCUONES_TRISECION.ConstantesK(A,x,B,y,C,z)
        EP,NP = FUNCUONES_TRISECION.CoordenadasP(EA,EB,EC,NA,NB,NC,K1,K2,K3)

        return EP,NP 

    print("\nPunto 5. Triseccion")
    print("\n-----------------------------------------")
    EA,NA = FUNCUONES_TRISECION.Coordenadas("A")
    print("\n-----------------------------------------")
    EB,NB = FUNCUONES_TRISECION.Coordenadas("B")
    print("\n-----------------------------------------")
    EC,NC = FUNCUONES_TRISECION.Coordenadas("C")
    print("\n-----------------------------------------")

    beta,theta,eta = FUNCUONES_TRISECION.AngulosABC(EA,NA,EB,NB,EC,NC)

    print("\nDigite cualquiera de las siguientes opciones: ")
    print("1: Digitar las direcciones horizontales de la triseccion")
    print("2: Digitar los angulos de la triseccion")
    opcion = 0
    opcion = int(input(print("Introduce la opcion: ")))

    if opcion == 1:

        print("\n-----------------------------------------")
        AB = FUNCUONES_TRISECION.Direcciones_Horizontales("AB")
        print("\n-----------------------------------------")
        AP = FUNCUONES_TRISECION.Direcciones_Horizontales("AP")
        print("\n-----------------------------------------")
        BC = FUNCUONES_TRISECION.Direcciones_Horizontales("BC")
        print("\n-----------------------------------------")
        BP = FUNCUONES_TRISECION.Direcciones_Horizontales("BP")
        print("\n-----------------------------------------")
        CP = FUNCUONES_TRISECION.Direcciones_Horizontales("CP")
        print("\n-----------------------------------------")
        CB = FUNCUONES_TRISECION.Direcciones_Horizontales("CB")
        print("\n-----------------------------------------")

        omega,rho = opcion1(AB,AP,BC,BP,CP,CB)
        EP,NP = datos(beta,theta,eta,omega,rho)
        print("\n----- Coordenadas del punto P -----")
        print(f"{EP},{NP}")

    elif opcion == 2:
        omega,rho = opcion2()
        print(f"Omega: {omega},rho: {rho}")
        EP,NP = datos(beta,theta,eta,omega,rho)
        print("\n----- Coordenadas del punto P -----")
        print(f"{EP},{NP}")

    else: 
        print("¡ERROR! No se puede ejecutar el programa") 