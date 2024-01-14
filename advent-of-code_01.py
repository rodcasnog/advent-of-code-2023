# import re
import regex as re

filename = './advent-of-code/advent-of-code_1.txt'
with open(filename, 'r') as file:
    data = file.read()

# data = """
# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# """

data = data.strip().split('\n')

# Part 1

# count = 0

# for line in data:
#     characters = list(line)
#     for char in characters:
#         if char in map(str, range(10)):
#             char1 = char
#             break
#     for char in characters[::-1]:
#         if char in map(str, range(10)):
#             char2 = char
#             break
#     count += int(char1 + char2)

# print(count)

# Part 2

count = 0

def find_number(char):
    if char in map(str, range(1, 10)):
        return char
    elif char == 'one':
        return '1'
    elif char == 'two':
        return '2'
    elif char == 'three':
        return '3'
    elif char == 'four':
        return '4'
    elif char == 'five':
        return '5'
    elif char == 'six':
        return '6'
    elif char == 'seven':
        return '7'
    elif char == 'eight':
        return '8'
    elif char == 'nine':
        return '9'

for line in data:
    # char1 = re.search(r"((one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|[0-9])", line).group()
    char1 = re.findall(r"((one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|[0-9])", line)[0][0]
    char2 = re.findall(r"((one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|[0-9])", line, overlapped=True)[-1][0]
    count += int(find_number(char1) + find_number(char2))
    print(count, line, int(find_number(char1) + find_number(char2)))

print(count)