import heapq
from itertools import count



def AStar(graph: dict, start : int, goal : int, heuristic: dict) -> list[str]:
    frontier = []
    if graph == {} or heuristic == {} :
        return []
    if start in heuristic.keys():
        # a tuple have first element is path and
        # second element is cost of that path
        heapq.heappush(frontier, ([(start, 0)], heuristic[start]))
    visited = set()

    while frontier:
         node = heapq.heappop(frontier)[0]
         print(node)
         current_state = node[-1][0]
         current_cost = node[-1][1]
         if current_state not in visited:
             if current_state == goal:
                 return [state[0] for state in node]
             visited.add(current_state)
             for neighbor in graph[current_state]:
                 next_state = neighbor[0]
                 next_cost = neighbor[1]
                 if neighbor not in visited:
                     total_cost = current_cost + next_cost
                     heapq.heappush(frontier, (node + [(next_state, total_cost)], total_cost + heuristic[next_state]))

    return []
