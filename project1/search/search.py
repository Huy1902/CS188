# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    stack = util.Stack()
    start = problem.getStartState()
    stack.push(start)
    expandedState = set()
    path = {start : None}
    direction = {}
    
    #save goal location
    cur = None

    while(stack.isEmpty() == False) :
        top = stack.pop()
        if(top not in expandedState) :
            if problem.isGoalState(top):
                cur = top
                break
            else:
                expandedState.add(top)
                for successor in problem.getSuccessors(top) :
                    #print(successor)
                    if successor[0] not in expandedState:
                        stack.push(successor[0])    
                        
                        path[successor[0]] = top
                        direction[successor[0]] = successor[1]
    #Path reconstruction
    
    listAction = []
    while(path[cur] is not None) :
        listAction.append(direction[cur])
        cur = path[cur]
    listAction.reverse()
    return listAction
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    start = problem.getStartState()
    queue.push(start)
    expandedState = set()
    expandedState.add(start)
    path = {start : None}
    direction = {}
    
    cur = None
    
    while(queue.isEmpty() == False) :
        first = queue.pop()
        if(problem.isGoalState(first)):
            cur = first
            break
        else:
            expandedState.add(first)
            for successor in problem.getSuccessors(first):
                if(successor[0] not in expandedState):
                    expandedState.add(successor[0])
                    queue.push(successor[0])
                    path[successor[0]] = first
                    #print(successor[0], ' ', first)
                    direction[successor[0]] = successor[1]
    listAction = []
    while(path[cur] is not None) :
        listAction.append(direction[cur])
        cur = path[cur]
    listAction.reverse()
    return listAction
    
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    getPathCost = lambda node : problem.getCostOfActions(node[1])
    priQueue = util.PriorityQueueWithFunction(getPathCost)
    
    start = problem.getStartState()
    priQueue.push((start, []))
    inQueue = set()
    # path = {start : None}
    # direction = []
    
    while not priQueue.isEmpty():
        node = priQueue.pop()
        frontier = node[0]
        path = node[1]
        # print('root path:', path)
        if not frontier in inQueue:
            inQueue.add(frontier)
            if(problem.isGoalState(frontier)):
                # path.reverse()
                # print(path)
                return path
            else:
                for successor in problem.getSuccessors(frontier):
                    location = successor[0]
                    if location not in inQueue:
                        direction = successor[1]
                        newPath = path[:]
                        newPath.append(direction)
                        newNode = ((location, newPath))
                        priQueue.push((newNode))
                        
                        # print(fringe, location, direction, newPath, path)
                        # direction[successor[0]] = successor[1]
                        
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
