import math
INFINITE_NEGATIVE = -100000

def value(state: int) -> int:
    print(f"state in value: {state}")
    if is_terminal(state):
        return game_tree[state]
    if is_max(state):
        return max_value(state)
    else:
        return exp_value(state)

def max_value(state: int) -> int:
    v = INFINITE_NEGATIVE
    for successor in getSuccessors(state):
        v = max(v, value(successor))
    return v


def is_terminal(state: int) -> bool:
    print(f"state: {state}, value: {game_tree[state]}, condition: {game_tree[state] != INFINITE_NEGATIVE}")
    return game_tree[state] != INFINITE_NEGATIVE
def is_max(state:int) -> bool:
    return int(math.log(state, 3)) % 2 == 0
def exp_value(state: int) -> int:
    v = 0
    for succesor in getSuccessors(state):
        p = probability(succesor)
        v += value(succesor) * p
    return v


def getSuccessors(state: int) -> list:
    successors = [i for i in range(state * 3, state * 3 + 3)]
    return successors


def probability(state: int) -> int:
    return probability_rate[state   ]

game_tree = [INFINITE_NEGATIVE] * 9
game_tree += [3, 12, 9, 2, 4, 6, 15, 6, 0]
print(game_tree)
probability_rate = [1/3] * len(game_tree)
print(value(1))
