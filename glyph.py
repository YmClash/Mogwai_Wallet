import hashlib
from typing import Dict

id_to_seed : Dict[int,str]= {}
id_to_symbol : Dict[int,int] = {}


USIZE = 64
SIZE = int(USIZE)
HALF_SIZE = SIZE // 2
ONE = 1
prefix =b""

def keccak256(data:bytes) -> bytes :
    return hashlib.sha3_256(data).digest()

def draw(id:int) -> str:
    a = int.from_bytes(keccak256(prefix + id_to_seed[id].encode()), "big")
    output = bytearray(USIZE *(USIZE+3)+30)
    c = 0
    for byte_ in prefix:
        output[c] = byte_
        c += 1

    x,y,v,value = 0,0,0,0

    mod = (a % 11) + 5

    if id_to_symbol[id] == 0:
        raise ValueError("Symbol not found")
    elif id_to_symbol[id] == 1:
        symbols = b".X/\\."
    elif id_to_symbol[id] == 2:
        symbols = b".+-|."


    for i in range(SIZE):
        y = (2*(i+HALF_SIZE)+1)
        if a % 3 == 1:
            y = -y
        elif a % 3 == 2 :
            y = abs(y)
        y = y * a
        for j in range(SIZE):
            x = (2 * (j - HALF_SIZE) + 1)
            if a %2 == 1:
                x = abs(x)
            x = x * a
            v = (x * y // ONE) % mod
            if v < 5 :
                value = char(symbols[v])
            else:
                value = ord(".")
            output[c] = value
            c += 1
            output[c:c+3] = b"%0A"
            c += 3

            return output.decode()


id_to_seed[1] = "YmC"
id_to_symbol[1] = 1

print(draw(1))



