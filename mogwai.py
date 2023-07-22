import os
from dotenv import load_dotenv
import gradio
from substrateinterface import SubstrateInterface, Keypair, MnemonicLanguageCode, KeypairType
from decimal import Decimal, getcontext
from mexc_sdk import Spot
import requests



load_dotenv()
key = os.getenv("COINMARKKETCAP_API_KEY")
mexc_client = Spot(api_key=os.getenv('MEXC_ACCESS_KEY'),api_secret=os.getenv('MEXC_SECRET_KEY'))



rpc_url = SubstrateInterface(url="wss://rpc-parachain.bajun.network")
# substrate = SubstrateInterface(url="ws://127.0.0.1:9944")
# etat = local_host.isConnected()
# print(etat)

ymc_address = ['5G6s3tvwCbQ7MZWYmUrZkG8iYxYwAG8usqM57yJF8bU8Dbvr']


def salut(name) :
    return f"Salut !!! {name}"


def get_balance(address) :
    url = "https://www.mexc.com/open/api/v2/market/ticker?symbol=BAJU_USDT"
    reponse = requests.get(url)
    data = reponse.json()
    prix_baju = float(data['data'][0]['last'])
    getcontext().prec = 15
    result = rpc_url.query('System', 'Account', [address])
    balance = Decimal(result.value['data']['free']) / Decimal(10 ** 12)
    balance_format = float(format(balance, '.2f'))
    print(type(result.value['data']['free']))
    balance_usd = prix_baju * balance_format
    return f"Votre Balance est de : {balance_format} Bajun  ~ {balance_usd:.2f}$ USD"


print(rpc_url.get_chain_head())

with gradio.Blocks(title="Ajuna Wallet Checker..by YmC") as app :
    adresse = gradio.Textbox(label="enter your address")
    nom = gradio.Textbox(label="enter your name")
    balance_output = gradio.Textbox(label="Balance")
    run_button = gradio.Button("RUN")
    salut_button = gradio.Button("Salu")
    run_button.click(fn=get_balance, inputs=adresse, outputs=balance_output)
    salut_button.click(fn=salut, inputs=nom, outputs=balance_output)

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
