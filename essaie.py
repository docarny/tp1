
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


print(dicothomie(0,4))
print(dicothomie(-1,6))
print(dicothomie(2,0.001))
print(dicothomie(0.1,0.00001))
print(dicothomie(10000,0.00001))




