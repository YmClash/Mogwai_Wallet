from glyph import mint

with open("seeds.txt", "r") as f:
    seeds = [line.strip() for line in f]

base_path = "../Mogwai_Wallet/Mog/"
for idx,seed in enumerate(seeds):
    #out_path = f'{base_path}output_{idx}.png'
    out_path_2 = f'{base_path}output_{seed[:5]}.png'    # utilisé les 5 premier caractère du seed pour le nom de l'image
    print(f"Generating {out_path_2}")
    mint(seed=seed, out_path=out_path_2)

print("Done")

#
# with open("seeds.txt", "w+b") as f :
#     seeds = [int(line[:-1]) for line in f]
#
# out_path = r"C:\Users\y_mc\PycharmProjects\Mogwai_Wallet\Mog"
# for seed in seeds :
#     mint(seed=seed, out_path=out_path)
#
#

