with open("./advent-of-code/advent-of-code_14.txt") as f:
    data = f.read()

# data = """
# O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....
# """

data = data.strip().split("\n")

# Part 1

# print(count_rocks(roll(data, 'north')))


# Part 2

def transpose(data):
    return list(map(''.join, zip(*data)))

count = 0

def roll_west(data):
    new_data = []
    for line in data:
        new_line = ['.'] * len(line)
        for i, char in enumerate(line):
            if char == '#':
                new_line[i] = '#'
            elif char == 'O':
                j = i
                while new_line[j] == '.':
                    j -= 1
                    if j < 0:
                        break
                new_line[j + 1] = 'O'
        new_data.append(''.join(new_line))
    return new_data

def roll(data, direction):
    if direction == 'west':
        return roll_west(data)
    elif direction == 'east':
        return [line2[::-1] for line2 in roll_west([line1[::-1] for line1 in data])]
    elif direction == 'north':
        return transpose(roll_west(transpose(data)))
    elif direction == 'south':
        return transpose(
                    [line1[::-1] for line1 in 
                            roll_west([line2[::-1] for line2 in transpose(data)])])

def roll_1_cycle(data):
    for direction in ['north', 'west', 'south', 'east']:
        data = roll(data, direction)
    return data

def roll_n_cycles(data, n):
    for i in range(n):
        data = roll_1_cycle(data)
    return data

def count_rocks(data):
    data = transpose(data)
    count = 0
    for line in data:
        for i, char in enumerate(line):
            if char == 'O':
                count += len(line) - i
    return count

start = 250
cycle_length = 1
cycle = []
found = False
moving_data = roll_n_cycles(data, start)
while not found:
    for i in range(2):
        moving_data = roll_1_cycle(moving_data)
        cycle.append(count_rocks(moving_data))
    if cycle[:cycle_length] == cycle[cycle_length:]:
        found = True
        print(cycle_length)
        break
    cycle_length += 1

total = 1000000000

while (total - start) % cycle_length != 0:
    start += 1
print(f"final sol = {count_rocks(roll_n_cycles(data, start))}")

cycles2plot = 10
to_plot = []
data = roll_n_cycles(data, start)
for n in range(1, cycle_length * cycles2plot + 2):
    data = roll_1_cycle(data)
    to_plot.append(count_rocks(data))

from matplotlib import pyplot as plt

begin = start + 1
end = start + 1 + cycle_length * cycles2plot + 1
plt.plot([n for n in range(begin, end)], to_plot)
plt.xticks([n for n in range(begin, end + 1, cycle_length )])
plt.grid()
plt.show()