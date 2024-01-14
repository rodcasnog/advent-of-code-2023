filename = './advent-of-code_24.txt'
with open(filename, 'r') as file:
    data = file.read()

# data = """
# 19, 13, 30 @ -2,  1, -2
# 18, 19, 22 @ -1, -1, -2
# 20, 25, 34 @ -2, -2, -4
# 12, 31, 28 @ -1, -2, -1
# 20, 19, 15 @  1, -5, -3
# """

data = data.strip().split('\n')
rays = {}

# Part 1

for i, line in enumerate(data):
    p, v = line.split(' @ ')
    rays[i] = (tuple(int(x.strip()) for x in p.split(','))[:2], tuple(int(x.strip()) for x in v.split(','))[:2])

a = 200000000000000
b = 400000000000000

intercepts = {}

for i in rays:
    px, py = rays[i][0]
    vx, vy = rays[i][1]
    intercepts[i] = -vy*px + vx*py

count = 0

for i in range(len(rays)):
    px1, py1 = rays[i][0]
    vx1, vy1 = rays[i][1]
    for j in range(i+1, len(rays)):
        px2, py2 = rays[j][0]
        vx2, vy2 = rays[j][1]
        delpx = px2 - px1
        delpy = py2 - py1
        q = (-delpx*vy1 + delpy*vx1)
        if (-vx2*vy1 + vy2*vx1)*q >= 0:
            continue
        if (-vx2*delpy + vy2*delpx)*q >= 0:
            continue
        intersection = (vx2*intercepts[i] - vx1*intercepts[j])/(-vx2*vy1 + vx1*vy2), \
                        (vy2*intercepts[i] - vy1*intercepts[j])/(-vx2*vy1 + vx1*vy2)
        if intersection[0] < a or intersection[0] > b or intersection[1] < a or intersection[1] > b:
            continue
        count += 1
