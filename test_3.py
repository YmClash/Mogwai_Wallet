import sr25519
import gradio
from substrateinterface import Keypair, MnemonicLanguageCode, KeypairType


def generate_mnemonic():
    keypair_seed = Keypair.generate_mnemonic(words=12, language_code=MnemonicLanguageCode.ENGLISH)

    return keypair_seed

def isvalide():
    validation = Keypair.validate_mnemonic(generate_mnemonic())
    return validation

def create_wallet():
    wallet = Keypair.create_from_mnemonic(generate_mnemonic,ss58_format=42,crypto_type=KeypairType.SR25519,language_code=MnemonicLanguageCode.ENGLISH)




with gradio.Blocks(title="Ajuna Wallet creator ") as demo:
    name = gradio.Textbox(label="Enter your name")
    output = gradio.Textbox(label="Phrase mnemonique ", )
    output_2 = gradio.Textbox(label="valide")
    output_3 = gradio.Textbox(label="Ajuna Wallet Adresse ")
    gen_button = gradio.Button("Genere Mno")
    valide_button = gradio.Button("Validation")
    create_wallet_button = gradio.Button("Create Ajuna wallet")
    gen_button.click(fn=generate_mnemonic, inputs=None, outputs=output, )
    valide_button.click(fn=isvalide,inputs=None,outputs=output_2)
    create_wallet_button.click


    demo.launch()

# keypair_seed = Keypair.generate_mnemonic(words=12,language_code=MnemonicLanguageCode.ENGLISH)
# valide = Keypair.validate_mnemonic(keypair_seed)
# keypair = Keypair.create_from_mnemonic(keypair_seed,ss58_format=42,crypto_type=KeypairType.SR22519,language_code=MnemonicLanguageCode.ENGLISH)

# print(f'keypair_seed: {keypair_seed}  :  is valide: {valide}')
# public_key = keypair.public_key
# private_key = keypair.private_key

#
# with open('cle_publique.txt','w') as f:
#     f.write(f"Keypair Seed: {keypair_seed}\n")
#     f.write(f"is valide : {valide} \n")
#     f.write(f"Keypair: {keypair}\n")
#     f.close()
#
#
# # print(f'Cle Publique : {keypair.public_key}')
# # print(f'Cle Privée : {keypair.private_key}')
# print()
# print()
#
# print("Keypair Seed enregistrées dans  le fichier cle_publique.txt")

demo = gradio.Interface(fn=generate_mnemonic, inputs=None, outputs=["text"],title="Ajuna Wallet creator ")

demo.launch()
