from itertools import product
from Crypto.Hash import keccak

kript = keccak.new(digest_bits=256)
kript.update(b'Mogwai')

print(kript.hexdigest())




MOTIF = {
    1: bytes.fromhex('2E582F5C2e'),
    2: bytes.fromhex('2E2B2D7C2e'),
    3: bytes.fromhex('2E2F5C2E2e'),
    4: bytes.fromhex('2E5C7C2D2F'),
    5: bytes.fromhex('2E4F7C2D2e'),
    6: bytes.fromhex('2E5C5C2E2e'),
    7: bytes.fromhex('2E237C2D2B'),
    8: bytes.fromhex('2E4F4F2E2e'),
    9: bytes.fromhex('2E232E2E2e'),
    10:bytes.fromhex('2E234F2E2e'),
}

print(MOTIF[1].decode(encoding='utf-8', errors='strict'))



#
#
# allo = b".X/<.+-|."
# print(allo.decode(encoding='utf-8', errors='strict'))
#
# hallo = {1 : bytes.fromhex('2E234F2E2e'),
#           2 : bytes.fromhex('2E2B2D7C2e')}
#
#
# print(hallo[2].decode(encoding='utf-8', errors='strict'))
#
# print(product('ABCD',repeat= 1))
#
#
