def racine(nombre):
    resultat = 0.0
    for i in range(nombre):  #donne une valeur de 0 a "nombre" pour i
        if i*i == nombre:   #si i^2 est egale a "nombre alors la fonction retourne i comme reponse
         return i
        elif i*i > nombre : #si i^2 est plus grand alors la fontion adition (i-1) a resultat, ce qui donne lunite de la racine
            resultat = i-1 + resultat
            return resultat #la fonction retourne le resultat et donc lunite de la racine

def decimale(n, nombre):
    valeur = racine(nombre)
    etape = 0.1

    for d in range(n):

        if











print(racine(3))
#print(racine(4))
#print(racine(9))
#print(racine(25))
#print(racine(64))