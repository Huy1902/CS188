# factorOperations.py
# -------------------
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

from typing import List

from bayesNet import Factor
import functools
from util import raiseNotDefined


def joinFactorsByVariableWithCallTracking(callTrackingList=None):
    def joinFactorsByVariable(factors: List[Factor], joinVariable: str):
        """
        Input factors is a list of factors.
        Input joinVariable is the variable to join on.

        This function performs a check that the variable that is being joined on 
        appears as an unconditioned variable in only one of the input factors.

        Then, it calls your joinFactors on all of the factors in factors that 
        contain that variable.

        Returns a tuple of 
        (factors not joined, resulting factor from joinFactors)
        """

        if not (callTrackingList is None):
            callTrackingList.append(('join', joinVariable))

        currentFactorsToJoin = [factor for factor in factors if joinVariable in factor.variablesSet()]
        currentFactorsNotToJoin = [factor for factor in factors if joinVariable not in factor.variablesSet()]

        # typecheck portion
        numVariableOnLeft = len(
            [factor for factor in currentFactorsToJoin if joinVariable in factor.unconditionedVariables()])
        if numVariableOnLeft > 1:
            print("Factor failed joinFactorsByVariable typecheck: ", factor)
            raise ValueError("The joinBy variable can only appear in one factor as an \nunconditioned variable. \n" +
                             "joinVariable: " + str(joinVariable) + "\n" +
                             ", ".join(map(str, [factor.unconditionedVariables() for factor in currentFactorsToJoin])))

        joinedFactor = joinFactors(currentFactorsToJoin)
        return currentFactorsNotToJoin, joinedFactor

    return joinFactorsByVariable


joinFactorsByVariable = joinFactorsByVariableWithCallTracking()


########### ########### ###########
########### QUESTION 2  ###########
########### ########### ###########

def joinFactors(factors: List[Factor]):
    """
    Input factors is a list of factors.  
    
    You should calculate the set of unconditioned variables and conditioned 
    variables for the join of those factors.

    Return a new factor that has those variables and whose probability entries 
    are product of the corresponding rows of the input factors.

    You may assume that the variableDomainsDict for all the input 
    factors are the same, since they come from the same BayesNet.

    joinFactors will only allow unconditionedVariables to appear in 
    one input factor (so their join is well defined).

    Hint: Factor methods that take an assignmentDict as input 
    (such as getProbability and setProbability) can handle 
    assignmentDicts that assign more variables than are in that factor.

    Useful functions:
    Factor.getAllPossibleAssignmentDicts
    Factor.getProbability
    Factor.setProbability
    Factor.unconditionedVariables
    Factor.conditionedVariables
    Factor.variableDomainsDict
    """

    # typecheck portion
    setsOfUnconditioned = [set(factor.unconditionedVariables()) for factor in factors]
    if len(factors) > 1:
        intersect = functools.reduce(lambda x, y: x & y, setsOfUnconditioned)
        if len(intersect) > 0:
            print("Factor failed joinFactors typecheck: ", factor)
            raise ValueError("unconditionedVariables can only appear in one factor. \n"
                             + "unconditionedVariables: " + str(intersect) +
                             "\nappear in more than one input factor.\n" +
                             "Input factors: \n" +
                             "\n".join(map(str, factors)))

    "*** YOUR CODE HERE ***"
    # Must use set if not many value will cause overflow
    factors = list(factors)
    unconditionedVariable = set(var for factor in factors for var in factor.unconditionedVariables())
    conditionedVariable = set(var for factor in factors for var in factor.conditionedVariables()
                           if var not in unconditionedVariable)
    variableDomainDict = factors[0].variableDomainsDict()
    joinFactor = Factor(unconditionedVariable, conditionedVariable, variableDomainDict)
    # print(joinFactor.getAllPossibleAssignmentDicts())
    for assignment in joinFactor.getAllPossibleAssignmentDicts():
        probability = 1.0
        for factor in factors:
            probability *= factor.getProbability(assignment)
        # print(assignment)
        Factor.setProbability(joinFactor, assignment, probability)
    return joinFactor
    "*** END YOUR CODE HERE ***"


########### ########### ###########
########### QUESTION 3  ###########
########### ########### ###########

def eliminateWithCallTracking(callTrackingList=None):
    def eliminate(factor: Factor, eliminationVariable: str):
        """
        Input factor is a single factor.
        Input eliminationVariable is the variable to eliminate from factor.
        eliminationVariable must be an unconditioned variable in factor.
        
        You should calculate the set of unconditioned variables and conditioned 
        variables for the factor obtained by eliminating the variable
        eliminationVariable.

        Return a new factor where all of the rows mentioning
        eliminationVariable are summed with rows that match
        assignments on the other variables.

        Useful functions:
        Factor.getAllPossibleAssignmentDicts
        Factor.getProbability
        Factor.setProbability
        Factor.unconditionedVariables
        Factor.conditionedVariables
        Factor.variableDomainsDict
        """
        # autograder tracking -- don't remove
        if not (callTrackingList is None):
            callTrackingList.append(('eliminate', eliminationVariable))

        # typecheck portion
        if eliminationVariable not in factor.unconditionedVariables():
            print("Factor failed eliminate typecheck: ", factor)
            raise ValueError("Elimination variable is not an unconditioned variable " \
                             + "in this factor\n" +
                             "eliminationVariable: " + str(eliminationVariable) + \
                             "\nunconditionedVariables:" + str(factor.unconditionedVariables()))

        if len(factor.unconditionedVariables()) == 1:
            print("Factor failed eliminate typecheck: ", factor)
            raise ValueError("Factor has only one unconditioned variable, so you " \
                             + "can't eliminate \nthat variable.\n" + \
                             "eliminationVariable:" + str(eliminationVariable) + "\n" + \
                             "unconditionedVariables: " + str(factor.unconditionedVariables()))

        "*** YOUR CODE HERE ***"
        # print(factor)
        variableDomainsDict = factor.variableDomainsDict()
        eliminationFactor = Factor(eliminationVariable, set(), variableDomainsDict)
        # print(eliminationFactor.getAllPossibleAssignmentDicts())
        # print(eliminationVariable)
        conditionedVariable = [var for var in factor.conditionedVariables()]
        unconditionedVariable = [var for var in factor.unconditionedVariables() if var != eliminationVariable]
        eliminatedFactor = Factor(unconditionedVariable, conditionedVariable, variableDomainsDict)
        for assignment in eliminatedFactor.getAllPossibleAssignmentDicts():
            # print(assignment)
            totalProbability = 0
            for eliminatedAssignment in eliminationFactor.getAllPossibleAssignmentDicts():
                assignment.update(eliminatedAssignment)
                totalProbability += factor.getProbability(assignment)
            # print(assignment)
            eliminatedFactor.setProbability(assignment, totalProbability)

        "*** END YOUR CODE HERE ***"
        return eliminatedFactor

    return eliminate


eliminate = eliminateWithCallTracking()
