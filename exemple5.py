import random
import time
# Conversion de types
valeur_entier = int("3")
valeur_flottant = float("3.41")

# Puissances et arrondi
valeur_puissance = pow(2, 3)
def rond(n,precison):
    valeur_arrondie = round(n,precison)
    return valeur_arrondie

print(rond(3.141516,4))

random.randrange(10,100000,1)
#print(random.randrange(10.00,100000.00,1.00))
random.uniform(10,100000)
print(random.uniform(10,100000))
random.random()
print(random.random())
time.process_time()