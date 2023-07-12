import random

numb = 1366618901674919
nn= "{:,.0f}".format(numb / 1000)
print(nn)
nnn = str(numb)



from decimal import Decimal, getcontext

# Définir la précision de decimal
getcontext().prec = 15

# Supposons que vous ayez cette quantité de crypto-monnaie

quantite_crypto = Decimal(1366618901674919) / Decimal(10**12)

# Formatage pour afficher avec 12 chiffres après la virgule
formatted_crypto = format(quantite_crypto, '.2f')

print(formatted_crypto)
