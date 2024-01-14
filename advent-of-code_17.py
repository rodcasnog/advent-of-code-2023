with open('./advent-of-code/advent-of-code_17.txt') as f:
    data = f.read()

# data = data.strip().split("\n")

# Part 1

import heapq
from collections import defaultdict

def dijkstra(data, start_i, start_j, end_i, end_j):

    data = [[float(i) for i in list(s)] for s in data.strip().split("\n")]

    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    distances = defaultdict(lambda: float('inf'))
    shortest_paths = defaultdict(list)
    priority_queue = []

    # Initialize starting points
    distances[(start_i, start_j)] = 0
    shortest_paths[(start_i, start_j)].append((start_i, start_j))
    heapq.heappush(priority_queue, (0, start_i, start_j))

    while priority_queue:
        dist, i, j = heapq.heappop(priority_queue)
        if (i, j) == (end_i, end_j):
            break
        
        # Expanding nodes
        for new_dir in directions:
            di, dj = directions[new_dir]
            ni, nj = i + di, j + dj
            if 0 <= ni < len(data) and 0 <= nj < len(data[0]):
                new_dist = dist + data[ni][nj]
                if new_dist < distances[(ni, nj)]:
                    distances[(ni, nj)] = new_dist
                    shortest_paths[(ni, nj)] = list(shortest_paths[(i, j)]) + [(ni, nj)]
                    heapq.heappush(priority_queue, (new_dist, ni, nj))

    return shortest_paths, distances

start_i, start_j = 0, 0
end_i, end_j = 140, 140

shortest_paths, distances = dijkstra(data, start_i, start_j, end_i, end_j)

goal_entries = [dist for ((i, j), dist) in distances.items() if i == 140 and j == 140]

# Find the minimum distance
min_distance = min(goal_entries)

# Retrieve the distance to the end goal
print(f"Distance to goal ({end_i}, {end_j}):", min_distance)

# Part 2

def modified_dijkstra(data, end_i, end_j, max_in_straight_line=float('inf'), min_in_straight_line=0):
    data = [[float(i) for i in list(s)] for s in data.strip().split("\n")]
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    distances = defaultdict(lambda: float('inf'))
    shortest_paths = defaultdict(list)
    priority_queue = []

    # Initialize starting points
    for dir in ['down', 'right']:
        di, dj = directions[dir]
        ni, nj = 0 + di, 0 + dj
        if 0 <= ni < len(data) and 0 <= nj < len(data[0]):
            initial_dist = data[ni][nj]
            heapq.heappush(priority_queue, (initial_dist, ni, nj, dir, 1))
            distances[(ni, nj, dir, 1)] = initial_dist
            shortest_paths[(ni, nj, dir, 1)].append((0, 0))
            shortest_paths[(ni, nj, dir, 1)].append((ni, nj))

    while priority_queue:
        dist, i, j, dir, steps = heapq.heappop(priority_queue)
        if (i, j) == (end_i, end_j):
            break
        if steps >= max_in_straight_line:
            continue
        # print((i, j, dir, steps), dist)
        # Expanding nodes
        for new_dir in directions:
            di, dj = directions[new_dir]
            ni, nj = i + di, j + dj
            if 0 <= ni < len(data) and 0 <= nj < len(data[0]):
                if new_dir != dir and steps < min_in_straight_line:
                    continue
                new_steps = 1 if new_dir != dir else steps + 1
                new_dist = dist + data[ni][nj]
                if new_dist < distances[(ni, nj, new_dir, new_steps)]:
                    distances[(ni, nj, new_dir, new_steps)] = new_dist
                    shortest_paths[(ni, nj, new_dir, new_steps)] = list(shortest_paths[(i, j, dir, steps)]) + [(ni, nj)]
                    heapq.heappush(priority_queue, (new_dist, ni, nj, new_dir, new_steps))

    return shortest_paths, distances

def get_distance_to_goal(distances, goal_i, goal_j):
    # Extract all entries for the goal node
    goal_entries = [(dist, dir, steps) for ((i, j, dir, steps), dist) in distances.items() if i == goal_i and j == goal_j]

    # If there are no entries for the goal, return None
    if not goal_entries:
        return None

    # Find the minimum distance
    min_distance = min(goal_entries, key=lambda x: x[0])[0]
    return min_distance

# Example usage
end_i, end_j = 140, 140
max_in_straight_line = 11
min_in_straight_line = 1

# Call the modified Dijkstra function
shortest_paths, distances = modified_dijkstra(data, end_i, end_j, max_in_straight_line, min_in_straight_line)

# Retrieve the distance to the end goal
distance_to_goal = get_distance_to_goal(distances, end_i, end_j)
print(f"Distance to goal ({end_i}, {end_j}):", distance_to_goal)