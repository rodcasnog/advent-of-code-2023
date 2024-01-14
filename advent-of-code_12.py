with open("./advent-of-code/advent-of-code_12.txt") as f:
    data = f.read()

# data = """
# ???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1
# """

# Part 1
data = [(x.split(' ')[0], tuple(map(int, x.split(' ')[1].split(',')))) for x in data.strip().split("\n")]

# Part 2
new_data = []
for line, numbers in data:
    new_data.append(('?'.join([line]*5), numbers*5))
data = new_data

def printer(func):
    def wrapper(*args):
        print(args, x := func(*args))
        return x
    return wrapper

known_vals = {}

def memoize(func):
    def wrapper(*args):
        if args not in known_vals:
            known_vals[args] = func(*args)
        # else:
        #     print(f'memoized: {args}-->{known_vals[args]}')
        return known_vals[args]
    return wrapper

import time
# from functools import cache

time1 = time.perf_counter()

# @printer
# @cache # this is faster than the memoize decorator, but i have coded the memoize decorator myself :)
@memoize
def count(line, numbers, trailing=0):

    if not line:
        # print('aaa', line, numbers, trailing, int( numbers == (trailing,)))
        return int(numbers == (trailing,))
    elif not numbers:
        return 1 if '#' not in set(line) else 0

    if line[0] == '?':
        return count('.' + line[1:], numbers, trailing) + count('#' + line[1:], numbers, trailing)

    if line[0] == '#':
        if numbers[0] >= trailing + 1:
            return count(line[1:], numbers, trailing + 1)
        else:
            return 0

    if trailing:
        if numbers[0] == trailing:
            return count(line, numbers[1:])
        else:
            return 0
    else:
        return count(line[1:], numbers)

print(sum([count(s[0], s[1]) for s in data]), len(known_vals))#,
    #   [count(s[0], s[1]) for s in data])

time2 = time.perf_counter()
print(time2 - time1)