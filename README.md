📌 Project Description
This project implements a Maze Solver using the A* Search Algorithm in Python. It finds a path from the starting point to the goal point in a maze.
The project also implements Breadth-First Search (BFS) to compare the performance of A* and BFS.
🎯 Objectives
Solve a maze using the A* algorithm.
Use Manhattan Distance as the heuristic.
Find the shortest path from start to goal.
Count the number of nodes expanded.
Compare A* with BFS.
🛠️ Technologies Used
Python 3
heapq – Priority Queue for A*
collections.deque – Queue for BFS
🧠 Algorithms Used
A* Search
A* calculates the priority using:
f(n) = g(n) + h(n)
Where:
g(n) = cost from the start node
h(n) = estimated cost to the goal
f(n) = total estimated cost
Manhattan Distance
The heuristic is calculated as:
h(n) = |x1 - x2| + |y1 - y2|
BFS
BFS explores the maze level by level and finds the shortest path when all movements have equal cost.
📂 Project Structure
Maze-Solver/
│
├── src/
│   └── maze_solver.py
│
└── README.md
▶️ How to Run
Install Python 3.
Open the project folder.
Open the src folder.
Run the Python file:
python maze_solver.py
📊 Output
The program displays:
A* path
A* path cost
A* nodes expanded
BFS path
BFS path cost
BFS nodes expanded
Comparison between A* and BFS
Example:
----- A* SEARCH -----
Path: [...]
Path Cost: ...
Nodes Expanded: ...

----- BFS SEARCH -----
Path: [...]
Path Cost: ...
Nodes Expanded: ...

----- COMPARISON -----
A* Nodes Expanded : ...
BFS Nodes Expanded: ...
💡 Applications
Robot path planning
Game navigation
GPS and route finding
AI search problems
Maze-solving applications
✅ Conclusion
The project demonstrates how A* can efficiently find a path through a maze using a heuristic. BFS is also implemented to compare the number of nodes explored by both algorithms.
