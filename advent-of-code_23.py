from queue import LifoQueue
from collections import defaultdict

filename = './advent-of-code_23.txt'
with open(filename, 'r') as file:
    data = file.read()

# data = """
# #.#####################
# #.......#########...###
# #######.#########.#.###
# ###.....#.>.>.###.#.###
# ###v#####.#v#.###.#.###
# ###.>...#.#.#.....#...#
# ###v###.#.#.#########.#
# ###...#.#.#.......#...#
# #####.#.#.#######.#.###
# #.....#.#.#.......#...#
# #.#####.#.#.#########v#
# #.#...#...#...###...>.#
# #.#.#v#######v###.###v#
# #...#.>.#...>.>.#.###.#
# #####v#.#.###v#.#.###.#
# #.....#...#...#.#.#...#
# #.#########.###.#.#.###
# #...###...#...#...#.###
# ###.###.#.###v#####v###
# #...#...#.#.>.>.#.>.###
# #.###.###.#.###.#.#v###
# #.....###...###...#...#
# #####################.#
# """

data = data.strip().split('\n')
width = len(data[0])
height = len(data)

start = (0, data[0].index('.'))
end = (height-1, data[height-1].index('.'))

q = LifoQueue()
q.put((start, start, 0))

# Find intersection tree

intersection_nodes = {}
visited = set()
visited_nodes = set()

while not q.empty():
    previous, current, dist = q.get()
    x, y = current
    visited.add(current)
    if end == current:
        intersection_nodes[(previous, current)] = dist
        continue
    elif [data[x - 1][y], data[x + 1][y], data[x][y - 1], data[x][y + 1]].count('#') <= 1:
        intersection_nodes[(previous, current)] = dist
        previous = current
        dist = 0
        visited_nodes.add(current)
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        x, y = current[0] + dx, current[1] + dy
        if 0 <= x < height and 0 <= y < width and data[x][y] != '#':
            if ((x,y) not in visited or ((x,y) in visited_nodes and (x,y) != previous))\
                                and (previous, (x,y)) not in visited_nodes\
                                and ((x,y), previous) not in visited_nodes: # this will enter a loop if two intersections are connected
                q.put((previous, (x, y), dist + 1))

nodes = {x[0] for x in intersection_nodes.keys()}.union({x[1] for x in intersection_nodes.keys()})
branches = {}
for node in nodes:
    branches[node] = {}
    for key in intersection_nodes.keys():
        if node == key[0]:
            branches[node][key[1]] = intersection_nodes[key]
        elif node == key[1]:
            branches[node][key[0]] = intersection_nodes[key]

q = LifoQueue()
q.put(({start}, start, 0))

explored = 0
best = 0

while not q.empty():
    explored += 1
    node_path, current_node, dist = q.get()
    if explored % 100000 == 0:
        print(explored, dist, best)
    if current_node == end:
        if best < dist: # if we don't put this inside here, it could find paths that don't end in the end node
            best = dist
        continue
        # best_path = node_path
    for node in branches[current_node].keys():
        if node not in node_path:
            q.put((node_path.union({node}), node, dist + branches[current_node][node]))

print(f"Best: {best}")
