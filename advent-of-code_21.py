with open('./advent-of-code/advent-of-code_21.txt') as f:
    data = f.read()

# Part 1 & 2
    
from collections import defaultdict

def get_map(data):
    garden_map = defaultdict(lambda: False)

    for i, line in enumerate(data.strip().splitlines()):
        for j, char in enumerate(line):
            if char == "#":
                garden_map[(i, j)] = True
            elif char == "S":
                start = (i, j)

    return start, garden_map

start, garden_map = get_map(data)

def compute_score(data, total_steps):
    width, height = len(data.strip().splitlines()[0]), len(data.strip().splitlines())
    start, garden_map = get_map(data)
    steps = 0
    reachable_in_steps = {start}

    while steps < total_steps:
        new = set()
        for i, j in reachable_in_steps:
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if not garden_map[((i + di)%height, (j + dj)%width)]:
                    new.add((i + di, j + dj))
        reachable_in_steps = new
        steps += 1

    return len(reachable_in_steps)

import heapq

def compute_score2(data, total_steps):
    width, height = len(data.strip().splitlines()[0]), len(data.strip().splitlines())
    (i, j), garden_map = get_map(data)

    distances = defaultdict(lambda: float('inf'))
    priority_queue = []

    # Initialize starting points
    distances[(i, j)] = 0
    heapq.heappush(priority_queue, (0, i, j))

    while priority_queue:
        dist, i, j = heapq.heappop(priority_queue)

        if dist > total_steps+20:
            distances.pop((i, j))
            break
        
        # Expanding nodes
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if not garden_map[(ni%height, nj%width)]:
                new_dist = dist + 1
                if new_dist < distances[(ni, nj)]:
                    distances[(ni, nj)] = new_dist
                    heapq.heappush(priority_queue, (new_dist, ni, nj))

    reachable = [k for k, v in distances.items() if (k[0] + k[1] + total_steps) % 2 == 0 and v <= total_steps]

    return len(reachable), distances

import numpy as np

vals = []
for n in range(3):
    total_steps = 65 + 131*n
    vals.append(compute_score2(data, total_steps)[0])

A = np.array([[ n**(2 - i) for i in range(3)] for n in range(3)])
b = np.array(vals)

coeffs = np.linalg.solve(A, b).astype(int)

n = 64

print('64:', compute_score2(data, 64)[0])

n = (26501365-65)//131

print(f'{n}:', sum([(coeffs[i])*n**(2-i) for i in range(3)]))