# A* Maze Solver Using Python

## Project Description

This project implements a Maze Solver using the A* Search Algorithm in Python. It finds a path from a starting point to a goal point in a maze.

The project also implements Breadth-First Search (BFS) to compare the performance of A* and BFS.

## Objectives

* To solve a maze using the A* Search Algorithm.
* To use Manhattan Distance as a heuristic.
* To find the shortest path from the start point to the goal point.
* To count the number of nodes expanded.
* To compare A* Search with BFS.

## Technologies Used

* Python 3
* heapq module
* collections.deque module

## Algorithms Used

### 1. A* Search Algorithm

A* is an informed search algorithm used to find the shortest path.

The evaluation function is:

f(n) = g(n) + h(n)

Where:

* g(n) = Cost from the starting node to the current node.
* h(n) = Estimated cost from the current node to the goal.
* f(n) = Total estimated cost.

### 2. Manhattan Distance

Manhattan Distance is used as the heuristic function.

Formula:

h(n) = |x1 - x2| + |y1 - y2|

It calculates the distance between the current cell and the goal cell without considering diagonal movement.

### 3. Breadth-First Search (BFS)

BFS explores the maze level by level. It uses a queue to store the nodes to be explored.

For a maze where every movement has the same cost, BFS can find the shortest path.

## Maze Representation

The maze is represented using a 2D list.

* 0 represents an open path.
* 1 represents a wall.

Example:

```
maze = [
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0]
]
```

Start Point: (0, 0)

Goal Point: (5, 5)

## Project Structure

```
Maze-Solver/
|
|-- src/
|   |-- maze_solver.py
|
|-- README.md
```

## How to Run

1. Install Python 3 on your computer.
2. Open the project folder.
3. Open the `src` folder.
4. Run the Python file using the following command:

   python maze_solver.py

## Output

The program displays the results of both A* and BFS algorithms.

The output includes:

* Path found by A*
* Path cost of A*
* Number of nodes expanded by A*
* Path found by BFS
* Path cost of BFS
* Number of nodes expanded by BFS
* Comparison between A* and BFS

Example output format:

```
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
```

## Advantages of A*

* Uses a heuristic to guide the search.
* Can find the shortest path when the heuristic is appropriate.
* Usually explores fewer unnecessary nodes than uninformed search.
* Useful for pathfinding problems.

## Applications

A* Search can be used in:

* Robot path planning
* Game navigation
* GPS and route finding
* Maze solving
* Artificial Intelligence
* Network routing

## Comparison of A* and BFS

| Feature        | A*                            | BFS                       |
| -------------- | ----------------------------- | ------------------------- |
| Search Type    | Informed Search               | Uninformed Search         |
| Heuristic      | Uses Manhattan Distance       | Does not use heuristic    |
| Data Structure | Priority Queue                | Queue                     |
| Shortest Path  | Yes, with suitable conditions | Yes, for equal edge costs |
| Node Expansion | Guided toward goal            | Level by level            |

## Conclusion

The A* Maze Solver demonstrates how Artificial Intelligence search algorithms can be used to solve pathfinding problems. A* uses the Manhattan Distance heuristic to guide the search toward the goal. BFS is also implemented to compare the number of nodes expanded and the path cost.

This project provides a simple understanding of A* Search, heuristic functions, BFS, and maze pathfinding using Python.

## Author

CSE (AIML) Student

