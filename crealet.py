import os
from dotenv import load_dotenv
from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3 import Web3, EthereumTesterProvider
from web3.middleware import construct_sign_and_send_raw_middleware


def create_account():
    w3=Web3()
    acc = w3.eth.account.create()
    print(f'private key :{w3.toHex(acc.privateKey)},account ={acc.address}')


w3= Web3(EthereumTesterProvider())

private_key = os.getenv("PRIVATE_KEY")

assert private_key is not None, "No private key set"
assert private_key.startswith("0x"),"Private key must start with 0x"

account : LocalAccount = Account.from_key(private_key)
w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))


print(f'Your hot wallet address is {account.address}')








