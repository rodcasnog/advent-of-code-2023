with open("./advent-of-code/advent-of-code_13.txt") as f:
    data = f.read()

# data = """
# #.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#
# """

data = [pattern.split('\n') for pattern in data.strip().split("\n\n")]

# # Part 1

# sums = 0

# def look_symms(pattern, mult = 1):
#     global sums
#     for j in range(len(pattern) // 2):
#         if pattern[j::-1] == pattern[j + 1:2 * (j + 1)]:
#             sums += (j + 1) * mult
#             return
#     for j in range(len(pattern) // 2, len(pattern) - 1):
#         if pattern[j:2 * j + 1 - len(pattern):-1] == pattern[j + 1:]:
#             sums += (j + 1) * mult
#             return

# def transpose(pattern):
#     return ["".join([pattern[i][j] for i in range(len(pattern))]) for j in range(len(pattern[0]))]

# for pattern in data:
#     look_symms(pattern, 100)
#     look_symms(transpose(pattern))

# print(sums)


# Part 2

sums = 0

def look_symms(pattern, mult = 1):
    global sums
    for j in range(len(pattern)-1):
        lines = list(zip(pattern[j::-1], pattern[j + 1:]))
        matches = 0
        for line1, line2 in lines:
            matches += sum([a == b for a, b in zip(line1, line2)])
        if matches == len(pattern[0]) * len(lines) - 1:
            sums += (j + 1) * mult
            return

def transpose(pattern):
    return ["".join([pattern[i][j] for i in range(len(pattern))]) for j in range(len(pattern[0]))]

for pattern in data:
    look_symms(pattern, 100)
    look_symms(transpose(pattern))

print(sums)