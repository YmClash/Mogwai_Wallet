from glyph import mint

with open("seeds.txt", "w+b") as f :
    seeds = [int(line[:-1]) for line in f]

out_path = "C:\Users\y_mc\PycharmProjects\Mogwai_Wallet\Mog"
for seed in seeds :
    mint(seed, out_path)
