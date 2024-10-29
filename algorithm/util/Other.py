import itertools

shoes = [x for x in range(0, 20)]

import random

count = 0
n = 1000000
for i in range(0, n):
    choose_shoe = []
    for x in range(0, 4):
        shoe = random.choice(shoes)
        if shoe not in choose_shoe:
            choose_shoe.append(shoe)
    # print(choose_shoe)
    comb = itertools.combinations(choose_shoe, 2)
    no_pair = True
    for x in comb:
        # print(x)
        if x[0] // 2 == x[1] // 2:
            no_pair = False
            break
    if not no_pair:
        count += 1


print(1 - count / n )