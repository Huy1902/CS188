# multiAgents.py
# --------------
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

from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"
        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood().asList()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        newScore = successorGameState.getScore()

        # print(f"----------\nnewPos: {newPos}")
        # print(f"newFood: {newFood}")
        # print(f"newGhostPos: {newGhostPos}")
        # print(f"newScaredTimes: {newScaredTimes}")
        if not newFood:
            return 10000
        distanceFood = [manhattanDistance(newPos, x) for x in newFood]

        minDistanceFood = min(distanceFood)

        # print(f"minDistanceFood: {minDistanceFood}")
        # print(f"newScore: {newScore}")
        # print(f"minDistanceGhost: {minDistanceGhost}\n---------------")
        return newScore * 10 - minDistanceFood


def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        numAgent = 0

        legalMoves = gameState.getLegalActions(0)
        bestScore = -10000
        bestMove = None
        for legalMove in legalMoves:
            successorGameState = gameState.generateSuccessor(numAgent, legalMove)
            score = self.value(0, numAgent + 1, successorGameState)
            if score > bestScore:
                bestScore = score
                bestMove = legalMove
        return bestMove

    def value(self, depth, numAgent, gameState: GameState) -> int:
        if numAgent == gameState.getNumAgents():
            numAgent = 0
            depth += 1
        if depth == self.depth:
            return self.evaluationFunction(gameState)

        if numAgent == 0:
            return self.maxValue(depth, numAgent, gameState)
        return self.minValue(depth, numAgent, gameState)

    def maxValue(self, depth, numAgent, gameState: GameState) -> int:
        legalMoves = gameState.getLegalActions(numAgent)
        if not legalMoves:
            return self.evaluationFunction(gameState)
        bestScore = -10000
        for legalMove in legalMoves:
            successorGameState = gameState.generateSuccessor(numAgent, legalMove)
            score = self.value(depth, numAgent + 1, successorGameState)
            if score > bestScore:
                bestScore = score
        # print(f"bestScore: {bestScore}")
        return bestScore

    def minValue(self, depth, numAgent, gameState: GameState) -> int:
        # print(f"numAgent: {numAgent}")
        legalMoves = gameState.getLegalActions(numAgent)
        if not legalMoves:
            return self.evaluationFunction(gameState)
        worstScore = 10000
        for legalMove in legalMoves:
            successorGameState = gameState.generateSuccessor(numAgent, legalMove)
            score = self.value(depth, numAgent + 1, successorGameState)
            if score < worstScore:
                worstScore = score
        # print(f"worstScore: {worstScore}")
        return worstScore


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        numAgent = 0
        max_best_option = -10000
        min_best_option = 10000
        legalMoves = gameState.getLegalActions(0)
        bestScore = -10000
        bestMove = None
        for legalMove in legalMoves:
            successorGameState = gameState.generateSuccessor(numAgent, legalMove)
            score = self.value(0, numAgent + 1, successorGameState, max_best_option, min_best_option)
            max_best_option = max(score, max_best_option)
            if score > bestScore:
                bestScore = score
                bestMove = legalMove
            if score > min_best_option:
                return bestMove
            max_best_option = max(score, max_best_option)
        return bestMove

    def value(self, depth, numAgent, gameState: GameState, max_best_option, min_best_option) -> int:
        if numAgent == gameState.getNumAgents():
            numAgent = 0
            depth += 1
        if depth == self.depth:
            return self.evaluationFunction(gameState)
        if numAgent == 0:
            return self.maxValue(depth, numAgent, gameState, max_best_option, min_best_option)
        return self.minValue(depth, numAgent, gameState, max_best_option, min_best_option)

    def maxValue(self, depth, numAgent, gameState: GameState, max_best_option, min_best_option) -> int:
        legalMoves = gameState.getLegalActions(numAgent)
        if not legalMoves:
            return self.evaluationFunction(gameState)
        bestScore = -10000
        for legalMove in legalMoves:
            successorGameState = gameState.generateSuccessor(numAgent, legalMove)
            score = self.value(depth, numAgent + 1, successorGameState, max_best_option, min_best_option)
            if score > bestScore:
                bestScore = score
            if score > min_best_option:
                return score
            max_best_option = max(score, max_best_option)
        # print(f"bestScore: {bestScore}")
        return bestScore

    def minValue(self, depth, numAgent, gameState: GameState, max_best_option, min_best_option) -> int:
        # print(f"numAgent: {numAgent}")
        legalMoves = gameState.getLegalActions(numAgent)
        if not legalMoves:
            return self.evaluationFunction(gameState)
        worstScore = 10000
        for legalMove in legalMoves:
            successorGameState = gameState.generateSuccessor(numAgent, legalMove)
            score = self.value(depth, numAgent + 1, successorGameState, max_best_option, min_best_option)
            if score < worstScore:
                worstScore = score
            if score < max_best_option:
                return score
            min_best_option = min(score, min_best_option)
        # print(f"worstScore: {worstScore}")
        return worstScore

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        numAgent = 0

        legalMoves = gameState.getLegalActions(0)
        bestScore = -10000
        bestMove = None
        for legalMove in legalMoves:
            successorGameState = gameState.generateSuccessor(numAgent, legalMove)
            score = self.value(0, numAgent + 1, successorGameState)
            if score > bestScore:
                bestScore = score
                bestMove = legalMove
        return bestMove

    def value(self, depth, numAgent, gameState: GameState) -> int:
        if numAgent == gameState.getNumAgents():
            numAgent = 0
            depth += 1
        if depth == self.depth:
            return self.evaluationFunction(gameState)

        if numAgent == 0:
            return self.maxValue(depth, numAgent, gameState)
        return self.expValue(depth, numAgent, gameState)

    def maxValue(self, depth, numAgent, gameState: GameState) -> int:
        legalMoves = gameState.getLegalActions(numAgent)
        if not legalMoves:
            return self.evaluationFunction(gameState)
        bestScore = -10000
        for legalMove in legalMoves:
            successorGameState = gameState.generateSuccessor(numAgent, legalMove)
            score = self.value(depth, numAgent + 1, successorGameState)
            if score > bestScore:
                bestScore = score
        # print(f"bestScore: {bestScore}")
        return bestScore

    def expValue(self, depth, numAgent, gameState: GameState) -> int:
        # print(f"numAgent: {numAgent}")
        legalMoves = gameState.getLegalActions(numAgent)
        if not legalMoves:
            return self.evaluationFunction(gameState)
        expectation = 0
        pdf = 1 / len(legalMoves)
        for legalMove in legalMoves:
            successorGameState = gameState.generateSuccessor(numAgent, legalMove)
            expectation += pdf * self.value(depth, numAgent + 1, successorGameState)
        # print(f"worstScore: {worstScore}")
        return expectation


def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    # Useful information you can extract from a GameState (pacman.py)

    "*** YOUR CODE HERE ***"
    pacmanPosition = currentGameState.getPacmanPosition()
    foodList = currentGameState.getFood().asList()
    ghostPositions = currentGameState.getGhostPositions()
    ghostStates = currentGameState.getGhostStates()
    score = currentGameState.getScore()

    # Compute the distance to the closest food item
    if foodList:
        distancesToFood = [manhattanDistance(pacmanPosition, food) for food in foodList]
        minFoodDistance = min(distancesToFood)
    else:
        minFoodDistance = 0

    # Compute the distances to the ghosts
    distancesToGhosts = [manhattanDistance(pacmanPosition, ghost) for ghost in ghostPositions]
    minGhostDistance = min(distancesToGhosts) if distancesToGhosts else 0

    # Compute the distances to the scared ghosts
    scaredGhostDistances = [manhattanDistance(pacmanPosition, ghostState.getPosition()) for ghostState in
                            ghostStates if ghostState.scaredTimer > 0]
    minScaredGhostDistance = min(scaredGhostDistances) if scaredGhostDistances else None

    if minScaredGhostDistance is not None:
        score += 200 / minScaredGhostDistance  # Encourage moving towards scared ghosts

    if minGhostDistance > 0:
        score -= 5 / minGhostDistance  # Discourage moving towards active ghosts

    if minFoodDistance > 0:
        score += 10 / minFoodDistance  # Encourage moving towards food

    score -= 20 * len(foodList)  # Discourage having too many foods left

    return score


# Abbreviation
better = betterEvaluationFunction
