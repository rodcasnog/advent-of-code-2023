from collections import defaultdict

filename = './advent-of-code/advent-of-code_3.txt'
with open(filename, 'r') as file:
    data = file.read()

# data = """
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..  
# """

data = data.strip().split('\n')

# Part 1

# height, width = len(data), len(data[0])
# numbers = {}
# numbers_pos = {}
# chars = defaultdict(list)

# for i in range(height):
#     chars[i] = []
#     numbers[i] = defaultdict(list)
#     numbers_pos[i] = defaultdict(list)
#     number_id = 0
#     j = 0
#     while j <width:
#         number = ''
#         while data[i][j] in map(str, range(10)):
#             number += data[i][j]
#             numbers_pos[i][number_id].append(j)
#             if j < width - 1:
#                 j += 1
#             else:
#                 break
#         if number:
#             numbers[i][number_id] = int(number)
#             number_id += 1
#         if data[i][j] in map(str, range(1, 10)):
#             break
#         if data[i][j] != '.':
#             chars[i].append(j) 
#         j += 1

# count = 0

# for i in range(height):
#     for number_id in numbers[i]:
#         for j in range(numbers_pos[i][number_id][0]-1, numbers_pos[i][number_id][-1]+2):
#             # print(i, numbers[i][number_id], j, chars[i]+chars[i-1]+chars[i+1])
#             if j in chars[i]+chars[i-1]+chars[i+1]:
#                 count += numbers[i][number_id]
#                 # print(numbers[i][number_id], count)
#                 break

# print(count)

# Part 2

height, width = len(data), len(data[0])
numbers = {}
numbers_pos = {}
gears = defaultdict(list)

for i in range(height):
    gears[i] = []
    numbers[i] = defaultdict(list)
    numbers_pos[i] = defaultdict(list)
    number_id = 0
    j = 0
    while j <width:
        number = ''
        while data[i][j] in map(str, range(10)):
            number += data[i][j]
            numbers_pos[i][number_id].append(j)
            if j < width - 1:
                j += 1
            else:
                break
        if number:
            numbers[i][number_id] = int(number)
            number_id += 1
        if data[i][j] in map(str, range(1, 10)):
            break
        if data[i][j] == '*':
            gears[i].append(j) 
        j += 1

number_grid = {}

for i in range(height):
    for number_id in numbers[i]:
        for j in numbers_pos[i][number_id]:
            number_grid[(i, j)] = numbers[i][number_id]

count = 0

for i in range(height):
    for j in gears[i]:
        num2check = set()
        for k in [i-1, i, i+1]:
            for l in [j-1, j, j+1]:
                if (k, l) in number_grid:
                    num2check.add(number_grid[(k, l)])
        if len(num2check) == 2:
            count += num2check.pop()*num2check.pop()

print(count)