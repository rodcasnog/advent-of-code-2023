with open('./advent-of-code/advent-of-code_9.txt') as f:
    data = f.read()

# Part 1

# data = """
# 0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45
# """

data = data.strip().split('\n')
data = [list(map(int, line.split())) for line in data]

diffs = {}
total1 = 0
total2 = 0

for i, line in enumerate(data):
    diffs[i] = {}
    j = 0
    diffs[i][j] = line
    while any(diffs[i][j]):
        j += 1
        diffs[i][j] = []
        for k in range(len(diffs[i][j-1])-1):
            diffs[i][j].append(diffs[i][j-1][k+1] - diffs[i][j-1][k])
    total1 += sum([diffs[i][j][-1] for j in range(len(diffs[i])-1)])
    temp_total2 = 0
    for j in range(len(diffs[i])):
        temp_total2 = - temp_total2 + diffs[i][len(diffs[i])-j-1][0]
    total2 += temp_total2

print(total1, total2)