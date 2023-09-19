from glyph import mint




with open("seeds.txt", "r") as f:
    seeds = [line.strip() for line in f]

base_path = "../Mogwai_Wallet/Mog/"
for idx,seed in enumerate(seeds):
    out_path = f'{base_path}output_{idx}.png'
    print(f"Generating {out_path}")
    mint(seed=seed, out_path=out_path)

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

