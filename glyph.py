import hashlib
import fastapi
from typing import Dict
from pathlib import Path
from matplotlib.patches import Circle, Rectangle


id_to_seed: Dict[int, str] = {}
id_to_symbol: Dict[int, int] = {}

USIZE = 64
SIZE = int(USIZE)
HALF_SIZE = SIZE // 2
ONE = int("1000000000",base=16)

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


def get_motif(id:int):
    index = id % 83

    if index < 20:
        scheme = 1
    elif index < 35:
        scheme = 2
    elif index < 48:
        scheme = 3
    elif index < 59:
        scheme = 4
    elif index < 68:
        scheme = 5
    elif index < 73:
        scheme = 6
    elif index < 77:
        scheme = 7
    elif index < 80:
        scheme = 8
    elif index < 82:
        scheme = 9
    else:
        scheme = 10

    return MOTIF[scheme]





def keccak256(data: bytes) -> bytes :
    return hashlib.sha3_256(data).digest()




def draw(keccak256: bytes):
    a = int.from_bytes(keccak256(id_to_seed[id].encode()), "big")
    output = bytearray(USIZE * (USIZE + 3) + 30)
    c = 0
    for byte_ in prefix :
        output[c] = byte_
        c += 1

    x, y, v, value = 0, 0, 0, 0

    mod = (a % 11) + 5

    # symbols = bytes([0x2E, 0x58, 0x2F, 0x5C, 0x2E, 0x2B, 0x2D, 0x7C, 0x2E, 0x2F,
    #                  0x5C, 0x2E, 0x2E, 0x5C, 0x7C, 0x2D, 0x2F, 0x4F, 0x7C, 0x2D,
    #                  0x2E, 0x5C, 0x5C, 0x2E, 0x23, 0x7C, 0x2D, 0x2B, 0x4F, 0x4F,
    #                  0x2E, 0x23, 0x2E, 0x2E, 0x2E, 0x23, 0x4F, 0x2E, 0x2E
    #                  ])[id_to_symbol[id]]

    if id_to_symbol[id] == 0 :
        raise ValueError("Symbol not found")
    elif id_to_symbol[id] == 1 :
        symbols = b".X/\\."
    elif id_to_symbol[id] == 2 :
        symbols = b".+-|."

    for i in range(SIZE) :
        y = (2 * (i + HALF_SIZE) + 1)
        if a % 3 == 1 :
            y = -y
        elif a % 3 == 2 :
            y = abs(y)
        y = y * a
        for j in range(SIZE) :
            x = (2 * (j - HALF_SIZE) + 1)
            if a % 2 == 1 :
                x = abs(x)
            x = x * a
            v = (x * y // ONE) % mod
            if v < 5 :
                value = (symbols[v])
            else :
                value = ord(".")
            output[c] = value
            c += 1
            output[c :c + 3] = b"%0A"
            c += 3

            return output.decode(encoding='utf-8', errors='strict')


id_to_seed[1] = "YmC"
id_to_symbol[1] = 1

print(draw(1))
