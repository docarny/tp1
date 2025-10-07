
def dicothomie(n):
    if n >= 1:
        def superieur(n,bas,haut):    # intervalle = {0,n}
            milieu = n / 2
            if milieu*milieu > n:
                bas = milieu
            elif milieu*milieu < n:
                haut = milieu
    else (0 < n < 1) :
        def inferieur(n):













