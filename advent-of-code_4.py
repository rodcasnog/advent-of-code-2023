filename = './advent-of-code/advent-of-code_4.txt'
with open(filename, 'r') as file:
    data = file.read()

# data = """
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# """

data = data.strip().split('\n')

# Part 1

# count = 0

# for line in data:
#     winning_numbers, playing_numbers = line.split(': ')[1].split(' | ')
#     winning_numbers = set(map(lambda x: int((x[0]+x[1]).strip()), zip(winning_numbers[::3], winning_numbers[1::3])))
#     playing_numbers = set(map(lambda x: int((x[0]+x[1]).strip()), zip(playing_numbers[::3], playing_numbers[1::3])))
#     n = len(winning_numbers.intersection(playing_numbers))
#     if n>0:
#         count += 2**(n-1)

# print(count)

# Part 2

wins = {}

for i, line in enumerate(data):
    winning_numbers, playing_numbers = line.split(': ')[1].split(' | ')
    winning_numbers = set(map(lambda x: int((x[0]+x[1]).strip()), zip(winning_numbers[::3], winning_numbers[1::3])))
    playing_numbers = set(map(lambda x: int((x[0]+x[1]).strip()), zip(playing_numbers[::3], playing_numbers[1::3])))
    n = len(winning_numbers.intersection(playing_numbers))
    wins[i] = n

cards = {}

for i in wins:
    cards[i] = 1

for i in wins:
    for j in range(1, wins[i]+1):
        cards[i+j] += cards[i]

print(sum(cards.values()))