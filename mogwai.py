import os
from dotenv import load_dotenv
from web3 import Web3
import gradio
from substrateinterface import SubstrateInterface, Keypair, MnemonicLanguageCode, KeypairType

rpc_url = SubstrateInterface(url="wss://rpc-parachain.bajun.network")
# substrate = SubstrateInterface(url="ws://127.0.0.1:9944")
# etat = local_host.isConnected()
# print(etat)

ymc_address = ['5G6s3tvwCbQ7MZWYmUrZkG8iYxYwAG8usqM57yJF8bU8Dbvr']

def salut(name):
    return f"Salut !!! {name}"

def get_balance(address):
    result = rpc_url.query('System', 'Account', [address])
    # print(result.value['data']['free'])
    return f"Votre Balance est de : {result.value['data']['free']:.20f} Bajun"



print(rpc_url.get_chain_head())

with gradio.Blocks(title="Ajuna Wallet Creator") as app:
    adresse = gradio.Textbox(label="enter your address")
    nom = gradio.Textbox(label="enter your name")
    balance_output = gradio.Textbox(label="Balance")
    run_button = gradio.Button("RUN")
    salut_button = gradio.Button("Salu")
    run_button.click(fn=get_balance,inputs=adresse,outputs=balance_output)
    salut_button.click(fn=salut,inputs=nom,outputs=balance_output)

    app.launch(debug=True)

# get_balance(liste_address[0])
get_balance(ymc_address[0])



# def transfer(dest):
#     call = rpc_url.compose_call(
#         call_module='Balances',
#         call_function='transfer',
#         call_params={
#             'dest': dest,
#             'value': 1 * 10 ** 15
#         }
#     )
#     keypair = Keypair.create_from_uri('//Alice')
#     extrinsic = rpc_url.create_signed_extrinsic(call=call, keypair=keypair)
#     recu = rpc_url.submit_extrinsic(extrinsic, wait_for_inclusion=True)
#
#     print(f"extrinsic : '{recu.extrinsic_hash}")
#     print(f"Block Hash: {recu.block_hash}")
#     print(f"Block Number: {recu.block_number}")
#
#
# print()

# for balance in liste_address:
#     print(f'{get_balance(balance)} Bajun ')
