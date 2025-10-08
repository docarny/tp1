
def dicothomie(n):
    if n >= 1:
        def superieur(n,bas,haut):    # intervalle = {0,n}
            milieu = n / 2
            if milieu*milieu > n:
                bas = milieu
            elif milieu*milieu < n:
                haut = milieu
    elif 0 < n < 1 :
        def inferieur(n,bas,haut):
            bas == n
            haut == 1
            milieu = (n+1) / 2
            if milieu*milieu > n:
                bas = milieu
            elif milieu*milieu < n:
              haut = milieu

    elif n==0:
        return 0
    else:
        return "la racine d'un nombre négatif est impossible"


print(dicothomie(0))
print(dicothomie(-1))
print(dicothomie(2))





