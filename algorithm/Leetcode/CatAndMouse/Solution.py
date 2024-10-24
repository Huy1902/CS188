# turns
from collections import deque

MOUSE = 0
CAT = 1
# states
MOUSE_WIN = 1
CAT_WIN = 2
DRAW = 0


class Solution:
    def catMouseGame(self, graph) -> int:
        n = len(graph)

        result = {}
        for i in range(1, n):
            result[i, i, CAT] = result[i, i, MOUSE] = CAT_WIN
            result[i, 0, CAT] = result[i, 0, MOUSE] = MOUSE_WIN

        degree = {}
        for cat in range(1, n):
            for mouse in range(1, n):
                degree[cat, mouse, MOUSE] = len(graph[mouse])
                degree[cat, mouse, CAT] = len(graph[cat]) - int(0 in graph[cat])
        q = deque(state for state in result.keys())

        while q:
            cat, mouse, turn = q.popleft()
            currentResult = result[cat, mouse, turn]

            if turn == MOUSE:
                prevStates = [(prevCat, mouse, CAT) for prevCat in graph[cat]]
            else:
                prevStates = [(cat, prevMouse, MOUSE) for prevMouse in graph[mouse]]

            for prevState in prevStates:
                if prevState in result:
                    continue
                prevCat, prevMouse, prevTurn = prevState
                if prevCat == 0:
                    continue
                degree[prevState] -= 1
                isWinner = ((currentResult == MOUSE_WIN and prevTurn == MOUSE) or
                            (currentResult == CAT_WIN and prevTurn == CAT))
                if isWinner or degree[prevState] == 0:
                    result[prevState] = currentResult
                    q.append(prevState)
        return result.get((2, 1, MOUSE), 0)

graph =[[2,3],[3,4],[0,4],[0,1],[1,2]]

print(Solution().catMouseGame(graph))