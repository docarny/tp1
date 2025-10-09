
def dicothomie(n,precision):
    if n >= 1:
        def superieur(n,bas,haut):    # intervalle = {0,n}
            milieu = (bas+haut)/2
            if milieu*milieu > n:
                bas = milieu
            elif milieu*milieu < n:
                haut = milieu
    elif 0 < n < 1 :
        def inferieur(n,precision):
            bas = n
            haut = 1
            milieu = (n+1) / 2
            while (haut - bas) > precision:

                if milieu*milieu > n:
                    haut = milieu
                elif milieu*milieu < n:
                    bas = milieu
            return round(((bas+haut)/2), precision)


    elif n==0:
        return 0
    else:
        return "la racine d'un nombre négatif est impossible"


#print(dicothomie(0,4))
#print(dicothomie(-1,6))
#print(dicothomie(2,4))
print(dicothomie(0.1,5))




