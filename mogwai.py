import os
from dotenv import load_dotenv
from web3 import Web3
from substrateinterface import SubstrateInterface, Keypair

rpc_url = SubstrateInterface(url="wss://rpc-parachain.bajun.network")
# substrate = SubstrateInterface(url="ws://127.0.0.1:9944")

# local_host = Web3.HTTPProvider(substrate)

# etat = local_host.isConnected()
# print(etat)


liste_address = ['5G6s3tvwCbQ7MZWYmUrZkG8iYxYwAG8usqM57yJF8bU8Dbvr',
                 # '5GrwvaEF5zXb26Fz9rcQpDWS57CtERHpNehXCPcNoHGKutQY',
                 # '5FHneW46xGXgs5mUiveU4sbTyGBzmstUspZC92UhjJM694ty',
                 # '5FLSigC9HGRKVhB9FiEo4Y3koPsNmBmLJbpXg2mp1hXcS59Y',
                 # '5DAAnrj7VHTznn2AWBemMuyBwZWs6FNFjdyVXUeYum3PTXFy',
                 # '5HGjWAeFDfFCWPsjFQdVV2Msvz2XtMktvgocEZcCj68kUMaw',
                 # '5CiPPseXPECbkjWCa6MnjNokrgYjMqmKndv2rSnekmSK2DjL',
                 ]


def get_balance(address):
    result = rpc_url.query('System', 'Account', [address])
    print(f"Votre Balance est de : {result.value['data']['free']}")


print(object())
print(rpc_url.get_chain_head())

print(rpc_url.get_metadata())


# get_balance(liste_address[0])


def transfer(dest):
    call = rpc_url.compose_call(
        call_module='Balances',
        call_function='transfer',
        call_params={
            'dest': dest,
            'value': 1 * 10 ** 15
        }
    )
    keypair = Keypair.create_from_uri('//Alice')
    extrinsic = rpc_url.create_signed_extrinsic(call=call, keypair=keypair)
    recu = rpc_url.submit_extrinsic(extrinsic, wait_for_inclusion=True)

    print(f"extrinsic : '{recu.extrinsic_hash}")
    print(f"Block Hash: {recu.block_hash}")
    print(f"Block Number: {recu.block_number}")


print()

for balance in liste_address:
    print(get_balance(balance))
