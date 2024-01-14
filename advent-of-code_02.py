filename = './advent-of-code/advent-of-code_2.txt'
with open(filename, 'r') as file:
    data = file.read()

# data = """
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# """

data = data.strip().split('\n')

# Part 1

# colour_limits = {'red': 12, 'green': 13, 'blue': 14}

# valid_count = 0

# for i, line in enumerate(data):
#     valid = True
#     i += 1
#     games = line.split(': ')[1].split('; ')
#     for game in games:
#         for cubes in game.split(', '):
#             num, colour = int(cubes.split(' ')[0]), cubes.split(' ')[1]
#             if num > colour_limits[colour]:
#                 valid = False
#     if valid:
#         valid_count += i

# print(valid_count)

# for line in data:
#     parts = line.split(': ')
#     games[parts[0][5:]] = []
#     for take in parts[1].split('; '):
#         bundle = []
#         for cubes in take.split(', '):
#             bundle.append((int(cubes.split(' ')[0]), cubes.split(' ')[1]))
#         games[parts[0][5:]].append(bundle)

# for game in games.keys():
#     print(game, games[game])

# Part 2

power_count = 0

def mult(lst):
    r = 1
    for x in lst:
        r *= x
    return r

for line in data:
    games = line.split(': ')[1].split('; ')
    min_num_colours = {'red': 0, 'green': 0, 'blue': 0}
    for game in games:
        for cubes in game.split(', '):
            num, colour = int(cubes.split(' ')[0]), cubes.split(' ')[1]
            if num > min_num_colours[colour]:
                min_num_colours[colour] = num
    power_count += mult(min_num_colours.values())

print(power_count)