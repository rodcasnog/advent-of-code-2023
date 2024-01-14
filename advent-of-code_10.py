with open('./advent-of-code/advent-of-code_10.txt') as f:
    data = f.read()

# Part 1

data = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""

pipe2dir = {('F', 'up'): 'right', ('F', 'left'): 'down',
            ('7', 'up'): 'left', ('7', 'right'): 'down',
            ('J', 'down'): 'left', ('J', 'right'): 'up',
            ('L', 'down'): 'right', ('L', 'left'): 'up',
            ('-', 'left'): 'left', ('-', 'right'): 'right',
            ('|', 'down'): 'down', ('|', 'up'): 'up'}

# dir2pipe = {}
# for (char, dir1), dir2 in pipe2dir.items():
#     dir2pipe[(dir1, dir2)] = char

dir2coord = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

data = data.strip().split('\n')
height, width = len(data), len(data[0])

for line in data:
    for char in line:
        if char == 'S':
            start = (data.index(line), line.index(char))
            break
steps = 1
for direction in ['up', 'down', 'left', 'right']:
    dx, dy = dir2coord[direction]
    x, y = start[0] + dx, start[1] + dy
    if 0 <= x < height and 0 <= y < width:
        if data[x][y] != '.':
            if (data[x][y], direction) in pipe2dir:
                break

path = [start]
while (x, y) != start:
    steps += 1
    direction = pipe2dir[(data[x][y], direction)]
    dx, dy = dir2coord[direction]
    x, y = x + dx, y + dy
    path.append((x, y))

# Part 2
    
path.append(start)
area = 0
for i in range(len(path) - 1):
    x1, y1 = path[i]
    x2, y2 = path[i + 1]
    area += (x2*y1-x1*y2)/2

print(steps//2, int(abs(area)-steps//2+1))