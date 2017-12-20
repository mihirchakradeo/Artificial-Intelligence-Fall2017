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

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
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
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        import util

        score = 0

        currFoodCount = currentGameState.getNumFood()
        succFoodCount = successorGameState.getNumFood()

        #if it is the goal state, return very high score
        if succFoodCount == 0:
            return 99999

        #following block of code calculates the periphery of the ghost,
        #and stores it in a list called ghostPeriphery

        dist = list()
        newFoodList = newFood.asList()
        xy1 = currentGameState.getPacmanPosition()
        ghostLocX, ghostLocY = currentGameState.getGhostPosition(1)
        ghostDist = manhattanDistance(newPos, (ghostLocX, ghostLocY))

        ghostPeriphery = [(ghostLocX, ghostLocY), (ghostLocX+1,ghostLocY), (ghostLocX-1,ghostLocY), (ghostLocX,ghostLocY+1), (ghostLocX,ghostLocY-1), (ghostLocX+1,ghostLocY+1), (ghostLocX-1,ghostLocY+1), (ghostLocX-1,ghostLocY-1), (ghostLocX+1,ghostLocY-1)]

        #if the newPos conincides with a location in the ghostPeriphery, then reduce the score by 15
        if newPos in ghostPeriphery:
            score -= 15

        #following block finds out distances to all food pellets and stores it in a list called dist
        flag = False
        for food in newFood.asList():
            if newPos == food:
                flag = True
            else:
                d = manhattanDistance(food, newPos)
                dist.append(d)

        #if next state is food, increase the score by 20
        if flag == True:
            score += 20

        #add the reciprocal of minimum distance to any food to the score
        temp = min(dist)
        score += 1.0/temp

        #increase the score by 10 if the state is a power pellet
        powerPelletLoc = currentGameState.getCapsules()
        if newPos in powerPelletLoc:
            score += 10

        if newScaredTimes:
            distToGhost = manhattanDistance(currentGameState.getPacmanPosition(), currentGameState.getGhostPosition(1))
            score += newScaredTimes[0]*distToGhost

        score += successorGameState.getScore()
        return score
        #return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
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

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

numNodesMM = 0
class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
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
        """
        "*** YOUR CODE HERE ***"
        import util
        #pacman makes first move
        move = self.maxPlyr(gameState, gameState.getNumAgents(), self.depth)
        legalMoves = gameState.getLegalActions()
        moveIndex = [index for index in range(len(legalMoves)) if legalMoves[index] == move[1]]
        #print "NUMNODES: ",numNodesMM
        return legalMoves[moveIndex[0]]

    "minPlayer tries out all legal action of each ghost by recursively calling itself"
    def minPlyr(self,state, agentIndex, numOfAgents, depth):
        minScore = 9999
        # if last min ghost has made the move
        if(agentIndex >= numOfAgents):
            #depth is one then return score of current state
            #else time for pacmans move
            if(depth == 1):
                return self.evaluationFunction(state)
            else:
                return self.maxPlyr(state, numOfAgents, depth - 1)
        else:
            legalMoves = state.getLegalActions(agentIndex)

            for action in legalMoves:
                #generate successor state
                successorGameState = state.generateSuccessor(agentIndex, action)
                global numNodesMM
                numNodesMM += 1
                #if generated move leads to terminal state then return score of
                #terminal state
                if(successorGameState.isLose() or successorGameState.isWin()):
                    tempScore = self.evaluationFunction(successorGameState)
                    if tempScore < minScore:
                        minScore = tempScore
                    continue
                #call the next ghost
                tempScore = self.minPlyr(successorGameState, agentIndex + 1, numOfAgents, depth)
                if tempScore < minScore:
                    minScore = tempScore
        return minScore
    "maxPlayer tries out all legal action of pacman by recursively calling itself"
    def maxPlyr(self, state, numOfAgents, depth):
        bestAction = None
        maxScore = -9999
        legalMoves = state.getLegalActions(0)

        for action in legalMoves:
            # generate successor state
            successorGameState = state.generateSuccessor(0, action)
            global numNodesMM
            numNodesMM += 1

            #next state is terminal state, return score
            if(successorGameState.isLose() or successorGameState.isWin()):
                tempScore = self.evaluationFunction(successorGameState)
                if tempScore > maxScore:
                    maxScore = tempScore
                    bestAction = action
                continue
            tempScore = self.minPlyr(successorGameState, 1, numOfAgents, depth)
            #take the best action till now
            if tempScore > maxScore:
                maxScore = tempScore
                bestAction = action
        if(depth == self.depth):
            return maxScore,bestAction
        else:
            return maxScore

        util.raiseNotDefined()

numNodes = 0
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        #pacman makes first move
        move = self.maxPlyr(gameState, gameState.getNumAgents(), self.depth, -9999, 9999)
        legalMoves = gameState.getLegalActions()
        moveIndex = [index for index in range(len(legalMoves)) if legalMoves[index] == move[1]]
        #print "Node Expanded: ",numNodes
        return legalMoves[moveIndex[0]]

    def minPlyr(self,state, agentIndex, numOfAgents, depth, alpha, beta):
        minScore = 9999
        # if last min ghost has made the move

        V = 9999
        if(agentIndex >= numOfAgents):
            #depth is one then return score of current state
            #else time for pacmans move
            if(depth == 1):
                return self.evaluationFunction(state)
            else:
                if alpha > beta:
                    return V
                return self.maxPlyr(state, numOfAgents, depth - 1, alpha, beta)
        else:
            legalMoves = state.getLegalActions(agentIndex)

            for action in legalMoves:
                #check if further successors have to be visited
                if alpha > beta:
                    return V
                successorGameState = state.generateSuccessor(agentIndex, action)
                global numNodes
                numNodes += 1
                #if generated move leads to terminal state then return score of
                #terminal state
                if(successorGameState.isLose() or successorGameState.isWin()):
                    tempScore = self.evaluationFunction(successorGameState)
                    if tempScore < V:
                        V = tempScore
                        #return V if less than alpha
                        if V < alpha:
                            return V
                        beta = min(beta, V)

                    continue
                #call the next ghost
                tempScore = self.minPlyr(successorGameState, agentIndex + 1, numOfAgents, depth, alpha, beta)
                if tempScore < V:
                    V = tempScore

                if V < alpha:
                    return V
                beta = min(beta, V)

        return V

    def maxPlyr(self, state, numOfAgents, depth, alpha, beta):
        bestAction = None
        maxScore = -9999
        V = -9999
        legalMoves = state.getLegalActions(0)

        for action in legalMoves:
            # generate successor state
            if alpha > beta:
                # return V, bestAction
                break

            successorGameState = state.generateSuccessor(0, action)
            global numNodes
            numNodes += 1
            #next state is terminal state, return score
            if(successorGameState.isLose() or successorGameState.isWin()):
                tempScore = self.evaluationFunction(successorGameState)
                if tempScore > V:
                    V = tempScore
                    bestAction = action
                    if V > beta:
                        return V
                    alpha = max(alpha, V)
                continue
            tempScore = self.minPlyr(successorGameState, 1, numOfAgents, depth, alpha, beta)
            #take the best action till now
            if tempScore > V:
                V = tempScore
                bestAction = action
            if V > beta:
                return V
            alpha = max(alpha, V)

        if(depth == self.depth):
            return V, bestAction
        else:
            return V
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        #pacman makes first move
        move = self.maxPlyr(gameState, gameState.getNumAgents(), self.depth)
        legalMoves = gameState.getLegalActions()
        moveIndex = [index for index in range(len(legalMoves)) if legalMoves[index] == move[1]]

        return legalMoves[moveIndex[0]]

    def expPlyr(self,state, agentIndex, numOfAgents, depth):
        minScore = 9999
        #variable to store average of scores of expecti states
        temp = 0.0
        # if last min ghost has made the move
        if(agentIndex >= numOfAgents):
            #depth is one then return score of current state
            #else time for pacmans move
            if(depth == 1):
                return self.evaluationFunction(state)
            else:
                return self.maxPlyr(state, numOfAgents, depth - 1)
        else:
            legalMoves = state.getLegalActions(agentIndex)

            for action in legalMoves:
                #generate successor state

                successorGameState = state.generateSuccessor(agentIndex, action)
                #if generated move leads to terminal state then return score of
                #terminal state
                if(successorGameState.isLose() or successorGameState.isWin()):
                    tempScore = self.evaluationFunction(successorGameState)
                    temp += tempScore
                    continue
                #call the next ghost

                #append value to temp for calculating average score
                tempScore = self.expPlyr(successorGameState, agentIndex + 1, numOfAgents, depth)
                temp += tempScore

        return temp/float(len(legalMoves))

    def maxPlyr(self, state, numOfAgents, depth):
        bestAction = None
        maxScore = -9999
        legalMoves = state.getLegalActions(0)

        for action in legalMoves:
            # generate successor state

            successorGameState = state.generateSuccessor(0, action)
            #next state is terminal state, return tempScore

            if(successorGameState.isLose() or successorGameState.isWin()):
                tempScore = self.evaluationFunction(successorGameState)
                #take the best action till now
                if tempScore > maxScore:
                    maxScore = tempScore
                    bestAction = action
                continue
            tempScore = self.expPlyr(successorGameState, 1, numOfAgents, depth)
            if tempScore > maxScore:
                maxScore = tempScore
                bestAction = action

        if(depth == self.depth):
            return maxScore,bestAction
        else:
            return maxScore
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"

    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
