def main(nombre):
    if nombre <0: return "la racine d'une nombre négatif est impossible"
    else:
        def racine(nombre):
            resultat = 0.0
            nombre = int(nombre) #transforme "nombre en enier pour pouvoir l'utiliser dans le calcule
            for i in range(nombre+1):  #donne une valeur de 0 à "nombre" pour i
                if i*i == nombre:   #si i^2 est égale a "nombre alors la fonction retourne i comme reponse
                    return i
                elif i*i > nombre : #si i^2 est plus grand alors la fontion adition (i-1) a resultat, ce qui donne lunite de la racine
                    return i-1 #la fonction retourne le resultat et donc lunite de la racine
        def decimale(nombre):   #fonction pour les decimales
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







print(main(-2))
print(main(0.1))
print(main(0))
print(main(9))
print(main(2))
print(main(3))
print(main(5))
print(main(6))
print(main(8))
print(main(64))
print(main(123))
print(main(10300))
