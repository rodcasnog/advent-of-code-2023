filename = './advent-of-code/advent-of-code_5.txt'
with open(filename, 'r') as file:
    data = file.read()

# data = """
# seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4
# """

data = data.strip().split('\n\n')

seeds = list(map(int, data[0].split(' ')[1:]))
# seed_to_soil = [list(map(int, data[1].split('\n')[i].split(' '))) for i in range(1, len(data[1].split('\n')))]
# soil_to_fertilizer = [list(map(int, data[2].split('\n')[i].split(' '))) for i in range(1, len(data[2].split('\n')))]
# fertilizer_to_water = [list(map(int, data[3].split('\n')[i].split(' '))) for i in range(1, len(data[3].split('\n')))]
# water_to_light = [list(map(int, data[4].split('\n')[i].split(' '))) for i in range(1, len(data[4].split('\n')))]
# light_to_temperature = [list(map(int, data[5].split('\n')[i].split(' '))) for i in range(1, len(data[5].split('\n')))]
# temperature_to_humidity = [list(map(int, data[6].split('\n')[i].split(' '))) for i in range(1, len(data[6].split('\n')))]
# humidity_to_location = [list(map(int, data[7].split('\n')[i].split(' '))) for i in range(1, len(data[7].split('\n')))]

trans = {}

for k in range(1, 8):
    trans[k] = sorted([list(map(int, data[k].split('\n')[i].split(' '))) for i in range(1, len(data[k].split('\n')))], key=lambda x: x[1])

# Part 1

# locations = []

# for seed in seeds:
#     # print('new seed: ', seed)
#     for k in trans:
#         for trans_range in trans[k]:
#             if seed >= trans_range[1] and seed < trans_range[1]+trans_range[2]:
#                 seed += trans_range[0] - trans_range[1]
#                 # print('transf', k)
#                 break
#         # print(seed)
#     locations.append(seed)

# print(min(locations))
    
# Part 2

piece_func = {}
piece_func2 = {}

for k in range(1, 8):
    piece_func[k] = {float('-inf'): 0}
    piece_func2[k] = {}
    for trans_range in trans[k]:
        piece_func[k][trans_range[1]] = trans_range[0] - trans_range[1]
        piece_func[k][trans_range[1] + trans_range[2]] = 0
    piece_func[k][float('inf')] = 0
    for i, key in enumerate(piece_func[k]):
        piece_func2[k][i] = (key, piece_func[k][key])

def compose(g, f):
    gof = {}
    key = 0
    for i in range(len(f)-1):
        a = f[i][0]
        b = f[i+1][0]
        for j in range(len(g)-1):
            c = g[j][0] - f[i][1]
            d = g[j+1][0] - f[i][1]
            if max(a, c) < min(b, d):
                gof[key] = (max(a, c), f[i][1] + g[j][1])
                key += 1
    # gof = dict(sorted(gof.items(), key=lambda x: x[1][0]))
    gof[len(gof)] = (float('inf'), 0)
    return gof

def f_eval(f, x):
    for i in range(len(f)-1):
        if x >= f[i][0] and x < f[i+1][0]:
            return x + f[i][1]
    return x

f = piece_func2[1]
for k in range(2, 8):
    f = compose(piece_func2[k], f)

points = []
for seed0, seed_range in zip(seeds[::2], seeds[1::2]):
    for x, t in f.values():
        if x >= seed0 and x < seed0 + seed_range:
            points.append(x + t)
    points.append(f_eval(f, seed0))
    points.append(f_eval(f, seed0 + seed_range - 1))

print(min(points))