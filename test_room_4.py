from itertools import product
allo = b".X/<.+-|."
print(allo.decode(encoding='utf-8', errors='strict'))

hallo = {1 : bytes.fromhex('2E234F2E2e'),
          2 : bytes.fromhex('2E2B2D7C2e')}


print(hallo[2].decode(encoding='utf-8', errors='strict'))

print(product('ABCD',repeat= 1))


