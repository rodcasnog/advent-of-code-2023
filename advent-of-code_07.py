with open('./advent-of-code/advent-of-code_7.txt') as f:
    data = f.read()

# data = """
# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483
# """

# Part 1

# card2val = {
#     'A': 14,
#     'K': 13,
#     'Q': 12,
#     'J': 11,
#     'T': 10,
# }

# data = dict(map(lambda x: (tuple(map(lambda l: card2val[l] if l in ['A', 'K', 'Q', 'J', 'T'] else int(l), x.split(' ')[0])),
#                            int(x.split(' ')[1])),
#                         data.strip().split('\n')))

# sorted_hands = sorted(data.keys(),
#                         key=lambda hand: tuple(
#                             sorted(
#                                 [sum([x==y for y in hand]) for x in set(hand)],
#                                 reverse=True
#                                 )
#                         ) + (hand,)
#                     )

# print(sum([(i+1)*data[hand] for i, hand in enumerate(sorted_hands)]))

# Part 2

card2val = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 1,
    'T': 10,
}

data = dict(map(lambda x: (tuple(map(lambda l: card2val[l] if l in ['A', 'K', 'Q', 'J', 'T'] else int(l), x.split(' ')[0])),
                           int(x.split(' ')[1])),
                        data.strip().split('\n')))

def order_hand(hand):
    if hand == (1,)*5:
        return (5, (1,)*5)
    max_card_without_J = max([x for x in set(hand) if x != 1], key=lambda x: hand.count(x))
    hand_with_J = [x if x != 1 else max_card_without_J for x in hand]
    return tuple(sorted([hand_with_J.count(x) for x in set(hand_with_J)], reverse=True)) + (hand,)

sorted_hands = sorted(data.keys(), key=order_hand)

print(sum([(i+1)*data[hand] for i, hand in enumerate(sorted_hands)]))