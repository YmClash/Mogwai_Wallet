import sr25519
from substrateinterface import Keypair,MnemonicLanguageCode ,KeypairType

keypair_seed = Keypair.generate_mnemonic(words=12,language_code=MnemonicLanguageCode.ENGLISH)
valide = Keypair.validate_mnemonic(keypair_seed)
keypair = Keypair.create_from_mnemonic(keypair_seed,ss58_format=42,crypto_type=KeypairType.SR22519,language_code=MnemonicLanguageCode.ENGLISH)

print(f'keypair_seed: {keypair_seed}  :  is valide: {valide}')
# public_key = keypair.public_key
# private_key = keypair.private_key

#
with open('cle_publique.txt','w') as f:
    f.write(f"Keypair Seed: {keypair_seed}\n")
    f.write(f"is valide : {valide} \n")
    f.write(f"Keypair: {keypair}\n")
    f.close()


# print(f'Cle Publique : {keypair.public_key}')
# print(f'Cle Privée : {keypair.private_key}')
print()
print()

print("Keypair Seed enregistrées dans  le fichier cle_publique.txt")

