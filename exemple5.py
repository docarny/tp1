import random
import time
# Conversion de types
#valeur_entier = int("3")
#valeur_flottant = float("3.41")

# Puissances et arrondi
#valeur_puissance = pow(2, 3)
#ef rond(n,precison):
  #  valeur_arrondie = round(n,precison)
   # return valeur_arrondie

#print(rond(3.141516,4))

import time

def calcul_intensif():
    '''
    N'essayez VRAIMENT pas de comprendre le code de cette fonction!
    Vous allez être en mesure de le comprendre à partir du cours sur les boucles.
    La seule chose qui est importante de savoir, c'est que cette fonction prend un
    certain temps pour s'exécuter (1 à 2 secondes en moyenne).
    '''
    total = 0
    for i in range(1, 40000000):  # 20 millions d'itérations
        total += i ** 0.5
    return total

tempA = time.monotonic_ns()
calcul_intensif()
tempB = time.monotonic_ns()

mystere = tempB - tempA # Expression intéressante
print(mystere)


#clock_gettime()
#gettimeofday()
#n = (random.uniform(10,10000) for a in range(100000))
#print(n)
#andom.randrange(10,100000,1)
#print(random.randrange(10.00,100000.00,1.00))
#random.uniform(10,100000)
#print(random.uniform(10,100000))
#random.random()
#print(random.random())
#time.process_time()