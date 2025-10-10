import math
def racine(nombre,base):
    nombre = int(nombre)
    base = int(base)
    if nombre < 0:raise ValueError("le nombre doit etre positif")
    else:
        for i in range(nombre+1):
            if pow(nombre,base) == nombre: return i
            elif pow(nombre,base) > nombre : return i-1
def nieme(base,nombre):
    if nombre < 0: return ValueError("le nombre doit etre positif")
    else:
        unite = racine(base,nombre)
        resultat = float(unite)
        etape = 0.1
        for a in range(12):
            for d in range(10):
                i = (d * etape) + resultat
                if pow(nombre,base) > nombre :
                    resultat += ((d-1) * etape)
                    break
            else :resultat += 9*etape
            etape/=10
        return resultat


print(nieme(8,3))
print(nieme(8,4))
print(nieme(8,5))