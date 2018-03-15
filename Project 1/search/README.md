# PROJECT 01 – REPORT 
 
### 1. Implement the depth-first search (DFS) algorithm in the depthFirstSearch function in search.py. To make your algorithm complete, write the graph search version of DFS, which avoids expanding any already visited states

Data format on Stack: Tuple <Position, Path till current node, Cost of the node>
Search Nodes expanded: 
- Tiny Maze – 15 
- Medium Maze – 146 
- Big Maze – 390 
 
### 2. Implement the breadth-first search (BFS) algorithm in the breadthFirstSearch function in search.py. Again, write a graph search algorithm that avoids expanding any already visited states. Test your code the same way you did for depth-first search

Data format on Queue: Tuple <Position, Path till current node, Cost of the node> in Queue 
Search Nodes expanded:
- Tiny Maze – 15 
- Medium Maze – 269 
- Big Maze – 620 
 
### 3. Implement the uniform-cost search (UCS) algorithm in the uniformCostSearch function in search.py

Data on Priority Queue: <Position, Path till current node, Total Cost> 
Priority: Total cost of path till the current node 
Search Nodes expanded:
- Medium Maze - 269 
- Big Maze - 620 
- Medium Dotted StayEastSearchAgent Maze – 186, cost - 1 
- Medium Dotted StayWestSearchAgent Maze – 108, cost – 68719479864 
 
### 4. Implement A* graph search in the empty function aStarSearch in search.py
Data on Priority Queue: <Position, Path till current node, g(n)> in Priority Queue, 
Priority: Total cost till the node + heuristic cost 
Search Nodes expanded: 
- Big Maze – 549 
 
### 5. Implement the CornersProblem search problem in searchAgents.py 
Our state representation includes position of pacman and a Boolean array which indicates which corners are visited. IsGoalState returns true when all four corners are visited i.e. when all the corner flags are true. The successor function will check if the current state is a corner and mark the corner flags. 
Search Nodes Expanded: 
- TinyCorners – 252
- MediumCorners – 1966
 
### 6. Implement a heuristic for the CornersProblem in cornersHeuristic. 
The heuristic is the sum of the minimum Euclidean distance from current position to nearest corner and from that corner to the next nearest corner. We are considering a relaxed version of the problem by ignoring the existence of walls. So, when we calculate the Euclidean distance between two points, it will always be less than or equal to the actual distance between the same two points. This implies that the heuristic is admissible as h(n) <= h*(n). 
Search Nodes Expanded: 
- MediumCorners - 1091
 
### 7. Fill in foodHeuristic in searchAgents.py with a consistent heuristic for the FoodSearchProblem
The heuristic is the sum of the minimum Euclidean distance from current position to nearest food and from that food to the next nearest food until all the food is consumed. Similar to the above problem we are considering a relaxed version of the problem by ignoring the existence of walls. So, when we calculate the Euclidean distance between two points, it will always be less than or equal to the actual distance between the same two points. This gives us the minimum path from current state till the last food. 
Search Nodes Expanded: 
- TrickySearch - 7227 
