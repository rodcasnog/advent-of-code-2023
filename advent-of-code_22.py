with open('./advent-of-code/advent-of-code_22.txt') as f:
    data = f.read()

def read_data(data):
    data = data.strip().split('\n')
    data = [x.split('~') for x in data]
    data = [[x.split(',') for x in y] for y in data]
    data = [tuple([tuple([int(z) for z in x]) for x in y]) for y in data]
    return dict(enumerate(data))

dict_data = read_data(data)

# Part 1

def get_varying_coordinate(brick):
    if brick[0][0] != brick[1][0]:
        return 0, [(x, brick[0][1], brick[0][2]) for x in range(brick[0][0], brick[1][0]+1)]
    elif brick[0][1] != brick[1][1]:
        return 1, [(brick[0][0], x, brick[0][2]) for x in range(brick[0][1], brick[1][1]+1)]
    else:
        return 2, [(brick[0][0], brick[0][1], x) for x in range(brick[0][2], brick[1][2]+1)]

from collections import defaultdict

def get_collapsed_data(dict_data):

    max_x = max([v[0][0] for v in dict_data.values()] + [v[1][0] for v in dict_data.values()])
    max_y = max([v[0][1] for v in dict_data.values()] + [v[1][1] for v in dict_data.values()])
    min_x = min([v[0][0] for v in dict_data.values()] + [v[1][0] for v in dict_data.values()])
    min_y = min([v[0][1] for v in dict_data.values()] + [v[1][1] for v in dict_data.values()])

    dict_data_sorted = dict(sorted(dict_data.items(), key=lambda x: x[1][0][2])).copy()
    dict_data_collapsed = dict()
    support = defaultdict(list)
    height = dict(((i,j),0) for i in range(min_x, max_x+1) for j in range(min_y, max_y+1))

    for k, v in dict_data_sorted.items():
        var_dim, range_brick = get_varying_coordinate(v)
        if var_dim == 2:
            dict_data_collapsed[k] = (v[0][:2] + (height[v[0][:2]]+1,),
                                        v[1][:2] + (height[v[0][:2]]+len(range_brick),))
            height[v[0][:2]] += len(range_brick)
        else:
            max_height = max([height[x[:2]] for x in range_brick])
            dict_data_collapsed[k] = (v[0][:2] + (max_height+1,),
                                        v[1][:2] + (max_height+1,))
            for x in range_brick:
                height[(x[:2])] = max_height+1
        
        for k2,v2 in dict_data_collapsed.items():
            if v2[1][2] == dict_data_collapsed[k][0][2]-1 and set([x[:2] for x in range_brick]).intersection(set([x[:2] for x in get_varying_coordinate(v2)[1]]))!=set():
                support[k].append(k2)
    
    return len(dict_data_collapsed) - len(set([v[0] for v in support.values() if len(v)==1])), support

print('Part 1:', get_collapsed_data(dict_data)[0])

# Part 2

def get_supporting(supports):
    supporting = defaultdict(list)
    for k, support_of_k in supports.items():
        for k2 in support_of_k:
            supporting[k2].append(k)
    return supporting

def compute_falling_bricks(k0, supports, supporting):
    moving_supports = {k0}
    active_supports = {k0}
    while active_supports:
        k = active_supports.pop()
        if supporting[k]:
            for k2 in supporting[k]:
                if moving_supports.issuperset(supports[k2]):
                    moving_supports.add(k2)
                    active_supports.add(k2)
    return len(moving_supports)-1 # excluding self

def compute_total_falling(dict_data):
    _, supports = get_collapsed_data(dict_data)
    supporting = get_supporting(supports)

    total = 0
    for k in dict_data:
        total += compute_falling_bricks(k, supports, supporting)
    return total

print('Part 2:', compute_total_falling(dict_data))