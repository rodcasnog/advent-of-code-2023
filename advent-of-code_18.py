with open('./advent-of-code/advent-of-code_18.txt') as f:
    data = f.read()

list_data = []

for line in data.strip().split("\n"):
    direction, steps, color = line.split(' ')
    list_data.append((direction, int(steps), color.strip('()')))

# Part 1

direction_to_coord = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, -1),
        'D': (0, 1),
    }

def process_data(data):
    direction_to_coord = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}
    list_data = []
    for line in data.strip().split("\n"):
        direction, steps, _ = line.split(' ')
        list_data.append((direction, int(steps)))

    i, j = (0, 0)
    path = [(0, 0)]

    for direction, steps in list_data:
        di, dj = direction_to_coord[direction]
        for _ in range(steps):
            i += di
            j += dj
            path.append((i, j))
    
    return list_data, path

def fill(path, start_i, start_j, size=1, draw_frequency=1000):
    direction_to_coord = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}
    min_i, min_j = map(min, zip(*path))

    count = 0
    interior = set()
    for i, j in path[:-1]:
        interior.add((i - min_i, j - min_j))
        count += 1

    active_nodes = [(start_i, start_j)]

    while active_nodes:
        i, j = active_nodes.pop(0)
        for new_dir in direction_to_coord:
            ni, nj = i + direction_to_coord[new_dir][0], j + direction_to_coord[new_dir][1]
            if ni < 0 or nj < 0:
                continue
            if (ni, nj) not in interior:
                active_nodes.append((ni, nj))
                interior.add((ni, nj))
                count += 1
    return interior, count

list_data, path = process_data(data)
interior, count = fill(path, 100, 100)
print(count)






# Part 2

# Unnecessarily complicated solution

def get_new_movements(movements_list, orientation=True):
        
    new_movements = []

    for movement_pair in list(zip(movements_list, movements_list[1:])) + [(movements_list[-1], movements_list[0])]:

        prev_dir, prev_steps = movement_pair[0]
        curr_dir, _ = movement_pair[1]

        if prev_dir == 'R':
            if curr_dir == 'U':
                new_movements.append((True, prev_steps))
            elif curr_dir == 'D':
                new_movements.append((False, prev_steps))
        elif prev_dir == 'L':
            if curr_dir == 'U':
                new_movements.append((False, prev_steps))
            elif curr_dir == 'D':
                new_movements.append((True, prev_steps))
        elif prev_dir == 'U':
            if curr_dir == 'L':
                new_movements.append((True, prev_steps))
            elif curr_dir == 'R':
                new_movements.append((False, prev_steps))
        elif prev_dir == 'D':
            if curr_dir == 'L':
                new_movements.append((False, prev_steps))
            elif curr_dir == 'R':
                new_movements.append((True, prev_steps))
    
    if not orientation:
        new_movements = [(not x, y) for x, y in new_movements]

    return new_movements

def get_edges_from_color(data):

    new_list_data = []

    direction_to_coord = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}
    digit_to_coord = {'2':'L', '0':'R', '3':'U', '1':'D'}

    for line in data.strip().split("\n"):
        s = line.split(' ')[2].strip('(#)')
        new_list_data.append((digit_to_coord[s[-1]], int(s[:-1], 16)))

    i, j = (0, 0)
    new_path = [(0, 0)]

    for direction, steps in new_list_data:
        di, dj = direction_to_coord[direction]
        i += di*steps
        j += dj*steps
        new_path.append((i, j))

    return new_list_data, new_path

def fill_alt(data):

    def make_pairs(movement_set):
        movements = list(movement_set)
        return list(zip(movements, movements[1:])) + [(movements[-1], movements[0])] + list(zip(movements, movements[1:]))

    def pop_times(movements, x, times):
        for _ in range(times):
            if x <= len(movements):
                movements.pop(x)
            else:
                movements.pop(0)
        return movements
    
    def roll(movements, x):
        return movements[x:] + movements[:x]
    
    def remove_piece(movements, x):
        m = roll(movements, x)
        temp_area = m[0][1] * min([m[1][1], m[-1][1]])
        if not m[0][0]:
            temp_area *= -1
        

        if m[1][1] > m[-1][1]:
            if (m[-2][0] == m[-1][0]):
                # print('a00')
                m[-3] = (not m[-3][0], m[-3][1])
                m[-2] = (m[-2][0], m[0][1] - m[-2][1])
                m[-1] = (m[1][0], m[1][1] - m[-1][1])
            else:
                # print('a01')
                m[-2] = (not m[-2][0], m[0][1] + m[-2][1])
                m[-1] = (m[1][0], m[1][1] - m[-1][1])
            m = pop_times(m, 0, 2)
        elif m[1][1] < m[-1][1]:
            m[-1] = (m[-1][0], m[-1][1] - m[1][1])
            if (m[1][0] == m[0][0]):
                # print('a10')
                m[0] = (m[0][0], m[0][1] - m[2][1])
            else:
                # print('a11')
                m[0] = (m[2][0], m[2][1] + m[0][1])
            m = pop_times(m, 1, 2)
        else:
            if (m[1][0] == m[0][0]) and (m[-2][0] == m[0][0]):
                # print('a20')
                m[-3] = (not m[-3][0], m[-3][1])
                m[2] = (m[-2][0], -m[2][1] + m[0][1] - m[-2][1])
            elif not (m[1][0] == m[0][0]) and (m[-2][0] == m[0][0]):
                # print('a21')
                m[-3] = (not m[-3][0], m[-3][1])
                m[2] = (not m[2][0], m[2][1] + m[0][1] - m[-2][1])
            elif (m[1][0] == m[0][0]) and not (m[-2][0] == m[0][0]):
                # print('a22')
                m[2] = (not m[2][0], -m[2][1] + m[0][1] + m[-2][1])
            elif not (m[1][0] == m[0][0]) and not (m[-2][0] == m[0][0]):
                # print('a23')
                m[2] = (m[2][0], m[2][1] + m[0][1] + m[-2][1])
            m = pop_times(m, 0, 2)
            m = pop_times(m, -1, 2)
            # print(m[-2:]+m[:3])
    
        return m, temp_area

    area = 0

    movements_list, _ = get_edges_from_color(data)
    movements = get_new_movements(movements_list, False)

    while len(movements) > 4:
        pairs = make_pairs(movements)
        x = min([ipair for ipair in enumerate(pairs) if ipair[1][0][0] == ipair[1][1][0]], key=lambda x: (x[1][1][1], x[0]))[0]+1 #+1 bc we are getting the first of the pair
        if x == len(movements):
            x = 0
        movements, temp_area = remove_piece(movements, x)
        area += temp_area

    area += movements[0][1] * movements[1][1]

    return area + sum([x[1] for x in movements_list]) // 2 + 1 # Pick's theorem

print(fill_alt(data))





# Simple solution

def get_abs_path(m):
    path = [(0, 0)]
    i, j = 0, 0
    for direction, steps in m:
        di, dj = direction_to_coord[direction]
        i += di*steps
        j += dj*steps
        path.append((i, j))
    return path

def fill2(data):

    area = 0

    m, _ = get_edges_from_color(data)
    abs_path = get_abs_path(m)[1:]

    for i, (dir, x) in enumerate(m):
        if dir == 'R':
            area += x * abs_path[i][1]
        elif dir == 'L':
            area -= x * abs_path[i][1]

    return abs(area) + sum([x[1] for x in m]) // 2 + 1
    
print(fill2(data))