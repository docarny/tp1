import math
def racine(base,nombre):
    nombre = int(nombre)
    base = int(base)
    if nombre < 0:raise ValueError("le nombre doit etre positif")
    else:
        for i in range(nombre+1):
            if pow(i,base) == nombre: return i
            elif pow(i,base) > nombre : return i-1
def nieme(nombre,base):
    if nombre < 0: return ValueError("le nombre doit etre positif")
    else:
        unite = racine(base,nombre)
        resultat = float(unite)
        etape = 0.1
        for a in range(20):
            for d in range(10):
                i = (d * etape) + resultat
                if pow(i,base) > nombre :
                    resultat += ((d-1) * etape)
                    break
            else :resultat += 9*etape
            etape/=10
        return resultat


def ndicothomie(n,precision,base):
    if n >= 1:
        def superieur(n,precision,base):    # intervalle = {0,n}
            bas = 0.0
            haut = n
            while (haut - bas) > precision:
                milieu = (haut+bas)/2
                if pow(milieu,base)  > n:
                     haut = milieu
                elif pow(milieu,base) < n:
                        bas = milieu
                else: return milieu
            return (bas+haut)/2
        return superieur(n,precision,base)
    elif 0 < n < 1 :
        def inferieur(n,precision,base):
            bas = n
            haut = 1.0
            while (haut - bas) > precision:
                milieu = (bas + haut) / 2
                if pow(milieu,base) > n:
                    haut = milieu
                elif pow(milieu,base) < n:
                    bas = milieu
                else: return milieu
            return (bas+haut)/2
        return inferieur(n,precision,base)


    elif n==0:
        return 0.0
    else:
        return "la racine d'un nombre négatif est impossible"

print(nieme(8,2))
print(nieme(8,3))
print(nieme(8,4))
print(nieme(9,2))
print(nieme(9,3))
print(nieme(9,4))
print(nieme(81,2))
print(nieme(81,3))
print(nieme(81,4))
print(nieme(123,2))
print(nieme(123,3))
print(nieme(123,4))
print(ndicothomie(8,0.000000001,2))
print(ndicothomie(8,0.000000001,3))
print(ndicothomie(8,0.000000001,4))
print(ndicothomie(9,0.000000001,2))
print(ndicothomie(9,0.000000001,3))
print(ndicothomie(9,0.000000001,4))
print(ndicothomie(81,0.000000001,2))
print(ndicothomie(81,0.000000001,3))
print(ndicothomie(81,0.000000001,4))
print(ndicothomie(123,0.000000001,2))
print(ndicothomie(123,0.000000001,3))
print(ndicothomie(123,0.000000001,4))



