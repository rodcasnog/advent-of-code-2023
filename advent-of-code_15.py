with open("./advent-of-code/advent-of-code_15.txt") as f:
    data = f.read()

# data = """
# rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
# """

data = data.strip().split(",")

# Part 1

def hash_(word):
    hash_ = 0
    for char in word:
        hash_ += ord(char)
        hash_ *= 17
    return hash_ % 256

count = 0
for word in data:
    count += hash_(word)

print(count)

# Part 2
    
from collections import defaultdict
# import re

boxes = defaultdict(dict)

for word in data:
    # label = re.sub(r'-[a-zA-Z]', '', word)
    if word[-1] == "-":
        label = word[:-1]
        boxes.get(hash_(label), {}).pop(label, 0)
    else:
        label = word[:-2]
        focal = int(word[-1])
        boxes[hash_(label)][label] = focal
    # print(boxes)

count = 0
for i, box in boxes.items():
    for j, focal in enumerate(box.values()):
        # print(i, j, focal, '-->', (i + 1) * (j + 1) * focal)
        count += (i + 1) * (j + 1) * focal
    
print(count)