import random
from collections import defaultdict

filename = './advent-of-code_25.txt'
with open(filename, 'r') as file:
    data = file.read()

# Part 1
    
# data = '''
# jqt: rhn xhk nvd
# rsh: frs pzl lsr
# xhk: hfx
# cmg: qnr nvd lhk bvb
# rhn: xhk bvb hfx
# bvb: xhk hfx
# pzl: lsr hfx nvd
# qnr: nvd
# ntq: jqt hfx bvb xhk
# nvd: lhk
# lsr: lhk
# rzs: qnr cmg lsr rsh
# frs: qnr lhk lsr
# '''
    
data = data.strip().split('\n')
edge_tree = {}
for line in data:
    line = line.split(':')
    edge_tree[line[0]] = line[1].strip().split(' ')

nodes = set()
for node in edge_tree:
    nodes.add(node)
    for node2 in edge_tree[node]:
        nodes.add(node2)

edges = set()
for node in edge_tree.keys():
    for edge in edge_tree[node]:
        edges.add((node, edge))

# Karger's algorithm
        
# print(len(nodes))
                
def karger(nodes, edges):
    edges = list(edges.copy())
    nodes = nodes.copy()
    merged2 = defaultdict(lambda: 1)
    while len(nodes) > 2:
        edge = random.sample(edges, 1)[0]
        edges.remove(edge)
        nodes.remove(edge[1])
        merged2[edge[0]] += merged2[edge[1]]
        for e in edges.copy():
            if e[0] == edge[1]:
                edges.append((edge[0], e[1]))
                edges.remove(e)
            elif e[1] == edge[1]:
                edges.append((e[0], edge[0]))
                edges.remove(e)
        edges = list(filter(lambda e: e[0] != e[1], edges))

    return edges, nodes, merged2

for i in range(100000):
    edges_, nodes_, merged2 = karger(nodes, edges)
    if i%100==0:
        print(i, len(edges_))
    if len(edges_)==3:
        print(i, merged2[nodes_.pop()]*merged2[nodes_.pop()])
        break