from math import sqrt, ceil, floor

# data = """
# Time:      7  15   30
# Distance:  9  40  200
# """

data = data.strip().split('\n')

# Part 1

# data = list(zip(*[line.split()[1:] for line in data]))

# Part 2

def word(x):
    li = ''
    for w in x:
        li += w
    return int(li)

data = [word(line.split()[1:]) for line in data]

i = 1
t, r = data
i *= ceil((t+sqrt(t**2-4*r))/2) - floor((t-sqrt(t**2-4*r))/2) - 1

print(i)