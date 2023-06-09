import random
import time
import numpy as np


liste = ['Spring', 'Summer', 'Fall', 'Winter']
liste_2 = [random.randint(1,50) for o in range(1,10000)]

debut = time.time()
for i in liste_2:
    print(i+1)
fin = time.time()

temps_execution = fin - debut

print(f'Temps d execution : {temps_execution} secondes')

debut_1 = time.time()
for e in liste_2:
    print(e+1)
fin_2 = time.time()

temps_execution_2 = fin_2 - debut_1

print(f'Temps d execution : {temps_execution_2} secondes')

print()
print()
print()

print(f'fonction 1 temps d execution : {temps_execution} secondes')
print(f'fonction 2 temps d execution : {temps_execution_2} secondes')





