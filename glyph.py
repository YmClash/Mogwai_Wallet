from typing import Dict
from pathlib import Path
import matplotlib.pyplot as plt
import random
from matplotlib.patches import Circle, Rectangle
from Crypto.Hash import keccak



# id_to_seed: Dict[int, str] = {}
# id_to_symbol: Dict[int, int] = {}
#
# USIZE = 64
# SIZE = int(USIZE)
# HALF_SIZE = SIZE // 2
# ONE = int("1000000000",base=16)

MOTIF = {
    1: "._|X/\*\#+",
    2: ".+-|.",
    3: ".X/\@\.",
    4: "./x\..",
    5: ".\|-/",
    6: ".O|-.",
    7: ".\~x\.*.",
    8: ".#|-+",
    9: ".OO..",
    10: ".#..#O.X.",
}

# ICI je  voudrai ajoute  un motif de couleur specifique
# a  chaque caractère  qui se trouve  dans  le dictonnaire MOTIF

COLOR_MOTIFS = {}

#une  coulour choisie hasard


def random_color():
    return (random.random(),random.random(),random.random())

#une  fonction qui  genere une couleur a partir du seed
def seed_color(seed):
    random.seed(get_seed(keccak_hash(seed)))
    return (random.random(),random.random(),random.random())



def keccak_hash(seed):
    k = keccak.new(digest_bits=256)
    k.update(seed.encode('utf-8'))
    return int(k.hexdigest(),16)

def get_seed(keccak_hash):
    return keccak_hash()


def get_motif(hash_value):
    index = hash_value % 83

    breakpoint = [20,35,48,59,68,73,77,80,82]
    motif = list(MOTIF.keys())

    for i,b in enumerate(breakpoint):
        if index < b:
            return MOTIF[motif[i]]


    # if index < 20:
    #     motif = 1
    # elif index < 35:
    #     motif = 2
    # elif index < 48:
    #     motif = 3
    # elif index < 59:
    #     motif = 4
    # elif index < 68:
    #     motif = 5
    # elif index < 73:
    #     motif = 6
    # elif index < 77:
    #     motif = 7
    # elif index < 80:
    #     motif = 8
    # elif index < 82:
    #     motif = 9
    # else:
    #     motif = 10
    #
    # return MOTIF[motif]
    #




def gen_glyph(seed):
    hash_value = keccak_hash(seed)
    mod = (hash_value % 11) + 5
    symbols = get_motif(hash_value)
    output = []

    for i in range(64):
        for j in range(64):
            v = (i * j * hash_value) % mod
            v %= len(symbols) # on controle soe v est dans la plage des symboles
            output.append(symbols[v])
        output.append("\n")

    return "".join(output)


def draw(art):

    fig, ax = plt.subplots(dpi=300,figsize=(5,5))

    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    draw_string = art.replace("\n", "")
    draw_string = [draw_string[i:i+64] for i in range(0, len(draw_string), 64)]

    ax.set_xlim(-1, 65)
    ax.set_ylim(65, -1)


    color = random_color()

    c = "k"
    lw = 0.9

    for x, chars in enumerate(draw_string):
        for y, char in enumerate(chars):
            if char == ".":
                continue
            elif char == "0":
                circle  = Circle((x+0.5, y+0.5), radius=0.5, color=color, fill=True)
                ax.add_patch(circle)
            elif char == "_":
                ax.plot([x, x+1], [y+0.5, y+0.5], color=color, lw=lw)
            elif char == "|":
                ax.plot([x+0.5, x+0.5], [y, y+1], color=color, lw=lw)
            elif char == "X":
                ax.plot([x, x+1], [y, y+1], color=color, lw=lw)
                ax.plot([x+1, x], [y, y+1], color=color, lw=lw)
            elif char == "/":
                ax.plot([x, x+1], [y+1, y], color=color, lw=lw) #revoir ici
            elif char == "\\":
                ax.plot([x, x+1], [y, y+1], color=color, lw=lw)
            elif char == "#":
                rect = Rectangle((x, y), width=1, height=1, color=color)
                ax.add_patch(rect)
            elif char == "+":
                ax.plot([x+0.5, x+0.5], [y, y+1], color=color, lw=lw)
                ax.plot([x, x+1], [y+0.5, y+0.5], color=color, lw=lw)
    return fig



def mint(seed,out_path):
    art = gen_glyph(seed)

    if len(set(art.replace("n",""))) == 1:
        raise ValueError("Maybe Glyph turn to Dust ")

    # draw_string = art.replace("\n","")
    # if len(set(draw_string)) == 1:
    #     raise ValueError("Maybe Glyph turn to Dust ")

    fig = draw(art)


    fig.savefig(out_path, dpi=300 , format='png', pad_inches=0.1)

    plt.close("all")


#
# if __name__ == "__main__" :
#         seed = "YMC Cest un Test One Piece"
#         out_path = "output.png"
#         mint(seed, out_path)

    # a = int.from_bytes(keccak256(id_to_seed[id].encode()), "big")
    # output = bytearray(USIZE * (USIZE + 3) + 30)
    # c = 0
    # for byte_ in prefix :
    #     output[c] = byte_
    #     c += 1
    #
    # x, y, v, value = 0, 0, 0, 0
    #
    # mod = (a % 11) + 5
    #
    # # symbols = bytes([0x2E, 0x58, 0x2F, 0x5C, 0x2E, 0x2B, 0x2D, 0x7C, 0x2E, 0x2F,
    # #                  0x5C, 0x2E, 0x2E, 0x5C, 0x7C, 0x2D, 0x2F, 0x4F, 0x7C, 0x2D,
    # #                  0x2E, 0x5C, 0x5C, 0x2E, 0x23, 0x7C, 0x2D, 0x2B, 0x4F, 0x4F,
    # #                  0x2E, 0x23, 0x2E, 0x2E, 0x2E, 0x23, 0x4F, 0x2E, 0x2E
    # #                  ])[id_to_symbol[id]]
    #
    # if id_to_symbol[id] == 0 :
    #     raise ValueError("Symbol not found")
    # elif id_to_symbol[id] == 1 :
    #     symbols = b".X/\\."
    # elif id_to_symbol[id] == 2 :
    #     symbols = b".+-|."
    #
    # for i in range(SIZE) :
    #     y = (2 * (i + HALF_SIZE) + 1)
    #     if a % 3 == 1 :
    #         y = -y
    #     elif a % 3 == 2 :
    #         y = abs(y)
    #     y = y * a
    #     for j in range(SIZE) :
    #         x = (2 * (j - HALF_SIZE) + 1)
    #         if a % 2 == 1 :
    #             x = abs(x)
    #         x = x * a
    #         v = (x * y // ONE) % mod
    #         if v < 5 :
    #             value = (symbols[v])
    #         else :
    #             value = ord(".")
    #         output[c] = value
    #         c += 1
    #         output[c :c + 3] = b"%0A"
    #         c += 3
    #
    #         return output.decode(encoding='utf-8', errors='strict')


# id_to_seed[1] = "YmC"
# id_to_symbol[1] = 1
#
# print(draw(1))
