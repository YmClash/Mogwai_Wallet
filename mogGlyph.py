from glyph import mint

with open("seeds.txt", "w+b") as f :
    seeds = [int(line[:-1]) for line in f]

out_path = r"C:\Users\y_mc\PycharmProjects\Mogwai_Wallet\mogwai"
for seed in seeds :
    mint(seed, out_path)
