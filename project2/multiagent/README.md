AI - Project 02: Multi-Agent Pac-Man Report 
 
Q1. Reflex Agent 
We calculated the score of the agent based on the following factors: 
If Pacman is in the periphery of the ghost, then deduct the score by 15 
If next state is a food state, then increase the score by 20 
If the next state is not a food state, take distance to closest food pellet and add it's reciprocal to score 
If the next state is a power pellet, then increase the score by 10 
If the newScaredTime value is is not zero, then increase the score by a factor of value of newScaredTime*distance to the ghost 
Average Score: 1272.2 
Win Rate: 10/10 
 
Q2. Minimax Agent 
Number of nodes expanded: 
 11,658 
Time taken: 
Finished running MinimaxAgent on smallClassic after 1 seconds. 
 
Q3. Alpha-Beta Pruning 
Number of nodes expanded: 9714 
Time Taken: Finished running AlphaBetaAgent on smallClassic after 0 seconds. 
 
Q4. Expectimax 
Number of nodes expanded: 11444 
Time Taken: Finished running ExpectimaxAgent on smallClassic after 1 seconds. 
Critical Analysis 
It can be seen that the number of nodes expanded decreased from 11,658 to 9714 after using Alpha-Beta pruning. That is, Alpha-Beta was able to successfully prune the branches. 
For the trapped classic game environment, Alpha-Beta Agent results in all losses, however, the Expectimax Agent wins 9/10 times. 
This happens because Alpha-Beta Agent finds out that the scenario is unwinnable and ends up running into the closest ghost to get a lesser bad score. 
