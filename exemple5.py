# Conversion de types
valeur_entier = int("3")
valeur_flottant = float("3.41")

# Puissances et arrondi
valeur_puissance = pow(2, 3)
def rond(n,precison):
    valeur_arrondie = round(n,precison)
    return valeur_arrondie

print(rond(3.141516,4))