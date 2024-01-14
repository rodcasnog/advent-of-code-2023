with open('./advent-of-code/advent-of-code_11.txt') as f:
    data = f.read()

# Part 1

# data = """
# ...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....
# """

data = data.strip().split('\n')
data = [list(line) for line in data]

height, width = len(data), len(data[0])

# new_data = []

# for row in range(height):
#     if set(data[row]) == {'.'}:
#         new_data.append(['.'] * width)
#     new_data.append((data[row]).copy())

# new_height = len(new_data)

# for col in range(width):
#     if set([data[row][col] for row in range(height)]) == {'.'}:
#         for row in range(new_height):
#             new_data[row].insert(col, '.')

# new_width = len(new_data[0])

# print('\n'.join(''.join(row) for row in new_data))


empty_rows = []
empty_cols = []
for row in range(height):
    if set(data[row]) == {'.'}:
        empty_rows.append(row)
for col in range(width):
    if set([data[row][col] for row in range(height)]) == {'.'}:
        empty_cols.append(col)

galaxies = []
for row in range(height):
    for col in range(width):
        if data[row][col] == '#':
            galaxies.append((row, col))

x_s = [galaxy[0] for galaxy in galaxies]
y_s = sorted([galaxy[1] for galaxy in galaxies])

distances_x = []
for i in range(len(x_s) - 1):
    next = x_s[i + 1] - x_s[i]
    if next>1:
        distances_x.append(next + 1000000-1)
    else:
        distances_x.append(next)
distances_y = []
for i in range(len(y_s) - 1):
    next = y_s[i + 1] - y_s[i]
    if next>1:
        distances_y.append(next + 1000000-1)
    else:
        distances_y.append(next)

sol = 0

for i in range(1, len(distances_x)+1):
    sol += distances_x[i-1] * i * (len(distances_x) + 1 - i)
for i in range(1, len(distances_y)+1):
    sol += distances_y[i-1] * i * (len(distances_y) + 1 - i)

print(sol)