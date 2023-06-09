from bitcoin import *
import os


file_name = str(input("Veuillez entre le Nom du fichier  : "))


# cree  et ouvrir un  fichier  un  fichier qui va contenir les information de notre  wallet
f = open(file_name,"w")


# cree une  cle Privé

private_key = random_key()
print("Cle Privée/Private Key : ", str(private_key))
print()
print()


# on cree une clee public a partir de la cle prive

public_key = privtopub(private_key)
print("Cle Public/Public Key : ", str(public_key))
print()
print()

# cree une adresse bitcoin à partir de la  cle public

address = pubtoaddr(public_key)
print(" L'adresse Bitcoin  est le  suivant ", str(address))
print()
print()

# Ecrire   les  information  sur  notre  Fichier  Txt
f.write(file_name + " Information "+'\n')
f.write("Wallet Adress : "+str(address)+'\n')
f.write("Public Key : "+str(public_key)+'\n')
f.write("Private Key : "+str(private_key)+'\n')
f.close()

print()

f = open(file_name,"r")
print(f.read())
f.close()





