with open("./advent-of-code/advent-of-code_20.txt") as f:
    data = f.read()

# data = """
# broadcaster -> a, b, c
# %a -> b
# %b -> c
# %c -> inv
# &inv -> a
# """

# data = """
# broadcaster -> a
# %a -> inv, con
# &inv -> b
# %b -> con
# &con -> output
# """

modules = list(map(lambda x: x.split(' -> '), data.strip().split("\n")))

module_desc = {}
module_asc = {}
module_type = {}
flipflop_state = {}
conj_state = {}

for module in modules:
    module[1] = module[1].split(', ')
    if module[0] == 'broadcaster':
        module_desc[module[0]] = module[1]
        module_type[module[0]] = 'b'
    else:
        module_desc[module[0][1:]] = module[1]
        module_type[module[0][1:]] = module[0][0]

for module, desc in module_desc.items():
    for i in desc:
        if i not in module_asc:
            module_asc[i] = []
        module_asc[i].append(module)

for module, asc in module_asc.items():
    if module not in module_type:
        continue
    if module_type[module] == '%':
        flipflop_state[module] = False
    elif module_type[module] == '&':
        conj_state[module] = {i: False for i in asc}

pulses = []

counts = {k:[] for k in ['qz', 'jx', 'tt', 'cq']}

def process_module(pulse, target, origin):
    global module_desc, module_asc, module_type, flipflop_state, conj_state, pulses, condition, iters
    if target in ['qz', 'jx', 'tt', 'cq'] and not pulse:
        counts[target].append(iters)
    if target not in module_type:
        return
    if module_type[target] == '%':
        if pulse:
            return
        else:
            new_pulse = not flipflop_state[target]
            flipflop_state[target] = not flipflop_state[target]
    elif module_type[target] == '&':
        conj_state[target][origin] = pulse
        if all(conj_state[target].values()):
            new_pulse = False
        else:
            new_pulse = True
    for desc in module_desc[target]:
        pulses.append((new_pulse, desc, target))

# low_count = 0
# high_count = 0

# def run():
#     global module_desc, module_asc, module_type, flipflop_state, conj_state, pulses, low_count, high_count
#     pulses = [(False, desc, 'broadcaster') for desc in module_desc['broadcaster']]
#     low_count += 1 # from button to broadcaster
#     while pulses:
#         pulse, target, origin = pulses.pop(0)
#         if pulse:
#             high_count += 1
#         else:
#             low_count += 1
#         process_module(pulse, target, origin)

# for i in range(1000):
#     run()

# # print(high_count, low_count, flipflop_state, conj_state, sep='\n')
# print(high_count * low_count)

# original_flipflop_state = flipflop_state.copy()
# original_conj_state = conj_state.copy()

# run()
# iters = 1

# while original_flipflop_state != flipflop_state or original_conj_state != conj_state:
#     run()
#     iters += 1
# print(iters)

# Part 2

def run():
    global module_desc, module_asc, module_type, flipflop_state, conj_state, pulses, low_count, high_count, condition
    pulses = [(False, desc, 'broadcaster') for desc in module_desc['broadcaster']]
    condition = False
    while pulses:
        process_module(*pulses.pop(0))

iters = 0
while iters<10000:
    iters += 1
    run()

c = 1
for k,v in counts.items():
    val = set([a-b for a,b in zip(v[1:], v)]).pop()
    c *= val
    print(k, val)

print(c)


# import graphviz

# dot = graphviz.Digraph('Advent of Code 2023 Day 20')
# dot.attr(rankdir='UD')
# dot.attr('node', shape='circle')

# for module, desc in module_desc.items():
#     if module_type[module] == 'b':
#         dot.node(module, shape='doublecircle')
#     elif module_type[module] == '%':
#         dot.node(module, shape='square')
#     elif module_type[module] == '&':
#         dot.node(module, shape='invtrapezium')

# for module, desc in module_desc.items():
#     for i in desc:
#         dot.edge(module, i)

# dot.render('advent-of-code/advent-of-code_20', view=True)