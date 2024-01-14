with open("./advent-of-code/advent-of-code_19.txt") as f:
    data = f.read()

# data = """
# px{a<2006:qkq,m>2090:A,rfg}
# pv{a>1716:R,A}
# lnx{m>1548:A,A}
# rfg{s<537:gd,x>2440:R,A}
# qs{s>3448:A,lnx}
# qkq{x<1416:A,crn}
# crn{x>2662:A,R}
# in{s<1351:px,qqz}
# qqz{s>2770:qs,m<1801:hdj,R}
# gd{a>3333:R,R}
# hdj{m>838:A,pv}

# {x=787,m=2655,a=1222,s=2876}
# {x=1679,m=44,a=2067,s=496}
# {x=2036,m=264,a=79,s=2244}
# {x=2461,m=1339,a=466,s=291}
# {x=2127,m=1623,a=2188,s=1013}
# """

workflows, parts = data.strip().split("\n\n")

workflows = {wf.split('{')[0] : wf.split('{')[1].strip('}').split(',') for wf in workflows.split("\n")}

parts = [tuple(int(l[2:]) for l in part.strip('{}').split(',')) for part in parts.split("\n")]

letter2num = {l:i for i,l in enumerate('xmas')}
num2letter = {i:l for i,l in enumerate('xmas')}

# Part 1

def process(wf_name, part):
    global workflows
    wf = workflows[wf_name]
    for i,test in enumerate(wf):
        if i == len(wf) - 1:
            return test
        elif test[1] == '>':
            condition = part[letter2num[test[0]]] > int(test.split(':')[0][2:])
        elif test[1] == '<':
            condition = part[letter2num[test[0]]] < int(test.split(':')[0][2:])
        if condition:
            return test.split(':')[1]

def run(part):
    global workflows
    wf_name = 'in'
    while wf_name not in ['R', 'A']:
        wf_name = process(wf_name, part)
    if wf_name == 'A':
        return True
    else:
        return False
    
accepted_parts = [part for part in parts if run(part)]
print(sum([sum(part) for part in accepted_parts]))

# Part 2

import copy

list_accepted = []

def traverse_node(wf_name, lower=[.5]*4, upper=[4000.5]*4):
    
    global workflows, list_accepted

    lower, upper = copy.deepcopy((lower, upper)) # copy to avoid sharing upper and lower between branches

    if wf_name == 'A':
        list_accepted.append((lower, upper))
        return
    elif wf_name == 'R':
        return
    
    wf = workflows[wf_name]

    for i,test in enumerate(wf):
        
        if i == len(wf) - 1:
            traverse_node(test, lower, upper)
        
        else:
            next_wf = test.split(':')[1]
            if test[1] == '>':
                new_sep = int(test.split(':')[0][2:]) + 0.5
                if upper[letter2num[test[0]]] > new_sep:
                    if lower[letter2num[test[0]]] < new_sep:
                        lower1 = lower.copy()
                        lower1[letter2num[test[0]]] = new_sep
                        traverse_node(next_wf, lower1, upper)
                        upper[letter2num[test[0]]] = new_sep
                    else:
                        traverse_node(next_wf, lower, upper)
            else:
                new_sep = int(test.split(':')[0][2:]) - 0.5
                if lower[letter2num[test[0]]] < new_sep:
                    if upper[letter2num[test[0]]] > new_sep:
                        upper1 = upper.copy()
                        upper1[letter2num[test[0]]] = new_sep
                        traverse_node(next_wf, lower, upper1)
                        lower[letter2num[test[0]]] = new_sep
                    else:
                        traverse_node(next_wf, lower, upper)

traverse_node('in')

sum = 0
for pair in list_accepted:
    volume = 1
    for dim in zip(*pair):
        volume *= int(dim[1] - dim[0])
    sum += volume
print(sum)