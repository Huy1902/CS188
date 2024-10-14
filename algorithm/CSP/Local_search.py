import math
from random import random

n = 50

states = [round(random() * 100) for _ in range(0, n)]

goalState = states.index(max(states))

print(goalState)

initialState = int(random() * n)

def getSuccessor(state):
    successors = []
    if state - 1 >= 0:
        successors.append(state - 1)
    if state + 1 < n:
        successors.append(state + 1)
    return successors

def getValue(state):
    return states[state]

def hill_climbing_search() -> int:
    current = initialState
    while current != goalState:
        successor = getSuccessor(current)
        highest = max(successor, key= getValue)
        if(getValue(highest) <= getValue(current)):
            return current
        current = highest
    return current

schedule = [ int((random() + _) * n / 5) for _ in range(n // 5, -1, -1)]
schedule.append(0)
print (schedule)
def stimulated_annealing() -> int:
    current = initialState
    for t in schedule:
        if t == 0:
            return current
        successor = getSuccessor(current)
        next = successor[int(random() * len(successor))]
        delta = getValue(next) - getValue(current)
        if delta > 0:
            current = next
        else:
            annealing_point = math.exp(delta / t)
            if annealing_point > random():
                current = next
    return 0


print("Hill: ", end=" ")
print(states)

print(f"Initial state: {initialState}")
print(f"Hill_climbing\nHighest expect: {goalState} \nActual: {hill_climbing_search()}\n"
      f"Value expect: {getValue(goalState)} \nActual: {getValue(hill_climbing_search())}")
result = stimulated_annealing()
print(f"Stimulated_annealing\nHighest expect: {goalState} \nActual: {result}\n"
      f"Value expect: {getValue(goalState)} \nActual: {getValue(result)}")
