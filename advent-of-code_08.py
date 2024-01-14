with open('./advent-of-code/advent-of-code_8.txt') as f:
    data = f.read()

# Part 1

# data = """
# RL

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)
# """

# data = data.strip().split('\n')

# instructions = data[0]
# ins2int = {'R': 1, 'L': 0}

# l = len(instructions)

# net = {}

# for line in data[2:]:
#     line = line.split(' = ')
#     net[line[0]] = tuple(line[1].replace('(', '').replace(')', '').split(', '))

# steps = 0
# first_node = 'AAA'
# last_node = 'ZZZ'
# current_node = first_node

# while current_node != last_node:
#     current_node = net[current_node][ins2int[instructions[steps % l]]]
#     steps += 1
#     print(current_node, steps)

# print(steps)

# Part 2

# data = """
# LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)
# """

data = data.strip().split('\n')

instructions = data[0]
ins2int = {'R': 1, 'L': 0}

l = len(instructions)

net = {}

for line in data[2:]:
    line = line.split(' = ')
    net[line[0]] = tuple(line[1].replace('(', '').replace(')', '').split(', '))

periods = {}

for first_node in net:

    if first_node[2] in ['A', 'Z']:
        steps = 0
        current_node = first_node
        while current_node[2] != 'Z' or not steps:
            current_node = net[current_node][ins2int[instructions[steps % l]]]
            steps += 1
            print(current_node, steps)
        if steps:
            periods[(first_node, current_node)] = steps

print(periods)

i_s = []

for path, steps in periods.items():
    if path[0][2] == 'A':
        i_s.append(steps)

from math import lcm

print(lcm(*i_s))