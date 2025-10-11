import math
def racine(nombre):
    """
La fonction racine a un nombre en base noté n qu'elle envoi dans différentes boucles for en fonction
de la valeur de celui-ci. Ensuite elle calcul i^2 et vérifie si le résultat est égal ou supérieur au nombre.
Enfin, lorsque la fonction à trouvé une valeur de i qui satisfait les conditions, elle renvoit soit i
(pour les racines parfaites comme 9 ou 81) ou i-1 pour les autres , car le carre de l'unite de la racine doit
être inférieur au nombre de la racine tel que la racine de 8 est 2,.... .


    """
    nombre = int(nombre)
    if nombre < 0:raise ValueError("le nombre doit etre positif")
    for i in range(nombre+1):
        if pow(i,2) == nombre:
            return i
        elif pow(i,2) > nombre :
            return i-1
def decimale(nombre):
    """
 La fonction décimale récupère le résultat de racine(nombre) et le stock comme un float. Ensuite d'une
 façon similsire, elle trie les nombres pour exclure les négatifs et soulever un message d'erreur.
 Elle utilise une boucle imbriqué de for pour calculer toute les décimales sans avoir a faire une fonction
 chaque niveau de précision. la ligne 38 permet à la fonction d'aditioner 9 * étape au résultat quand aucun
 autre chiffre ne fonctione. la ligne 39 elle permet de passer au prochain niveau de précision
    """
    if nombre < 0: return ValueError("le nombre doit etre positif")
    else:
        unite = racine(nombre)
        resultat = float(unite)
        etape = 0.1
        for a in range(6):
            for d in range(10):
                i = (d * etape) + resultat
                if pow(i,2) > nombre :
                    resultat += ((d-1) * etape)
                    break
            else :
                resultat += 9*etape
            etape/=10
        return resultat

print(decimale(0))    # 0.0
print(decimale(0.1))  # 0.31622776601683794
print(decimale(0.2))  # 0.4472135954999579
print(decimale(0.9))  # 0.9486832980505138
print(decimale(8))    # 2.8284271247461903
print(decimale(9))    # 3.0
print(decimale(81))   # 9.0
print(decimale(123))  # 11.090536506409418
print(decimale(999))  # 31.606961258558215
print(decimale(-3))   # Doit lever une exception










