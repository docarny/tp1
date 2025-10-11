import random
import time
import math

def racine(nombre):
    nombre = int(nombre)
    if nombre < 0:raise ValueError("le nombre doit etre positif")
    for i in range(nombre+1):
        if i*i == nombre:
            return i
        elif i*i > nombre :
            return i-1
def decimale(nombre):
    if nombre < 0: return ValueError("le nombre doit etre positif")
    else:
        unite = racine(nombre)
        resultat = float(unite)
        etape = 0.1
        for a in range(6):
            for d in range(10):
                i = (d * etape) + resultat
                if i*i > nombre :
                    resultat += ((d-1) * etape)
                    break
            else :
                resultat += 9*etape
            etape/=10
        return resultat

def dicothomie(n,precision):
    if n >= 1:
        def superieur(n,precision):    # intervalle = {0,n}
            bas = 0.0
            haut = n
            while (haut - bas) > precision:
                milieu = (haut+bas)/2
                if milieu*milieu > n:
                     haut = milieu
                elif milieu*milieu < n:
                        bas = milieu
            return (bas+haut)/2
        return superieur(n,precision)
    elif 0 < n < 1 :
        def inferieur(n,precision):
            bas = n
            haut = 1.0
            while (haut - bas) > precision:
                milieu = (bas + haut) / 2
                if milieu*milieu > n:
                    haut = milieu
                elif milieu*milieu < n:
                    bas = milieu
            return (bas+haut)/2
        return inferieur(n,precision)


    elif n==0:
        return 0
    else:
        return "la racine d'un nombre négatif est impossible"
def calcul_intensif():
    """
    calcul 100000 fois la racine d'un nombre aléatoire entre 10 et 10000 en utilisant la fonction decimale

    """
    for n in range(100000):
        n=random.uniform(10,10000)
        decimale(n)
tempA = time.monotonic_ns()
calcul_intensif()
tempB = time.monotonic_ns()
tempS = tempB - tempA
def calcul_intensif2():
    """
        calcul 100000 fois la racine d'un nombre aléatoire entre 10 et 10000 en utilisant la fonction
        dicothomie

        """
    for n in range(100000):
        n=random.uniform(10,10000)
        dicothomie(n,0.0000001)
tempA = time.monotonic_ns()
calcul_intensif2()
tempB = time.monotonic_ns()
tempS1 = tempB - tempA
def calcul_intensif3():
    for n in range(100000):
        """
            calcul 100000 fois la racine d'un nombre aléatoire entre 10 et 10000 en utilisant la fonction 
            math.sqrt

            """
        n=random.uniform(10,10000)
        math.sqrt(n)
tempA = time.monotonic_ns()
calcul_intensif3()
tempB = time.monotonic_ns()
tempS2 = tempB - tempA
print("Résultats des performances :")
print(f"Méthode 1 (chiffre par chiffre) : Temps total ={tempS*0.000001:.0f} ms, temps moyen = {(tempS/100000)*0.000001:.4f} ms ")
print(f"Méthode 2 (dichotomie)          : Temps total ={tempS1*0.000001:.0f} ms, temps moyen = {(tempS1/100000)*0.000001:.4f} ms ")
print(f"Méthode 3 (math.sqrt)           : Temps total ={tempS2*0.000001:.0f} ms, temps moyen = {(tempS2/100000)*0.000001:.4f} ms ")