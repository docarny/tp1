import random
import time
import math

def racine(nombre):
    nombre = int(nombre) #transforme "nombre en enier pour pouvoir l'utiliser dans le calcule
    if nombre < 0:raise ValueError("le nombre doit etre positif")
    for i in range(nombre+1):  #donne une valeur de 0 à "nombre" pour i
        if i*i == nombre:   #si i^2 est égale a "nombre alors la fonction retourne i comme reponse
            return i
        elif i*i > nombre : #si i^2 est plus grand alors la fontion adition (i-1) a resultat, ce qui donne lunite de la racine
            return i-1 #la fonction retourne le resultat et donc lunite de la racine
def decimale(nombre):   #fonction pour les decimales
    if nombre < 0: return ValueError("le nombre doit etre positif")
    else:
        unite = racine(nombre)  #appelle le resultat de la fonction racinez(nombre)
        resultat = float(unite) #transforme le resultat en unite float
        etape = 0.1  #pour avoir le niveau de précision
        for a in range(6): #nombre de décimale
            for d in range(10):  #permet tout les chiffres
                i = (d * etape) + resultat # donne la valeur du niveau de précision ex: 2.1 et l'assigne a i
                if i*i > nombre :
                    resultat += ((d-1) * etape) # si i^2 est superieur a "nombre" alors on prend la valeur de d d'avant puis on le multiplie par le noveau de precision
                    break
            else :
                resultat += 9*etape  #si on ne trouve pas le chiffre, alors c'est forcément 9 donc on ajoute 9* la precision à résultat
            etape/=10 # passe au prochain niveau de précision
        return resultat #retourne le résultat

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
    for n in range(100000):
        n=random.uniform(10,10000)
        decimale(n)
# #for n in range(100000):
#    # n=random.uniform(10,10000)
#     print(dicothomie(n,0.00000000001))
# for n in range(100000):
#     n=random.uniform(10,10000)
#     print(math.sqrt(n))
tempA = time.monotonic_ns()
calcul_intensif()
tempB = time.monotonic_ns()
tempS = tempB - tempA
print(tempS)

#time.perf_counter()
#print(time.perf_counter())
#print(dicothomie(10,0.00001))
#print(decimale(100002))
#random.uniform(10,100000)
#dicothomie(random.uniform(10,100000),0.00001)
#print(dicothomie(random.uniform(10,100000),0.00001))
#time.process_time_ns()
#print(math.sqrt(4))
#print(time.process_time())
