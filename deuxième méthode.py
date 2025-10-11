def dicothomie(n,precision):
    """
   La fonction dicothomie prend une valeur de precision en plus du nombre don l'ont cherche la racine.
   Elle commence par trié n en fonction de son intervale [0,n],[0<n<1] et de si n est égale a 0 ou négatifs.
   Ensuite dans les deux cas le calcule est le même. on donne la valeur approprié de bas et haut en fonction
   l'intervalle puis on effectue une boucle while jusqua ce que la différence des bornes soit inférieurs à
   la précision. le calcul en lui même est très similaire a la première méthode. elle vérifie si milieu^2
   est inférieur ou supérieur a n puis admet ,le haut ou le bas, égale à milieu en focntion du résultat.
   enfin la fonction renvoi bas+haut / 2 avec la nouvelle valeur affecté. lorsque le but est atteint, la
   fonction retourne la valeur de la sous fonction pour pouvoir etre éventuellement utiliser.

    """
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
        return 0.0
    else:
        return "la racine d'un nombre négatif est impossible"


print(dicothomie(0,0.0000001))    # 0.0
print(dicothomie(0.1,0.0000001))  # 0.31622776601683794
print(dicothomie(0.2,0.0000001))  # 0.4472135954999579
print(dicothomie(0.9,0.0000001))  # 0.9486832980505138
print(dicothomie(8,0.0000001))    # 2.8284271247461903
print(dicothomie(9,0.0000001))    # 3.0
print(dicothomie(81,0.0000001))   # 9.0
print(dicothomie(123,0.0000001))  # 11.090536506409418
print(dicothomie(999,0.0000001))  # 31.606961258558215
print(dicothomie(-3,0.0000001))   # Doit lever une exception