
    [0, 1, 1, 1, 0, 1],from collections import deque
import heapq

# 0 = open path, 1 = wall
maze = [
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0]
]

start = (0, 0)
goal = (5, 5)

# Manhattan Distance Heuristic
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


# Get valid neighbouring cells
def get_neighbors(node):
    r, c = node
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc

        if (0 <= nr < len(maze) and
            0 <= nc < len(maze[0]) and
            maze[nr][nc] == 0):
            yield (nr, nc)


# A* Algorithm
def astar():
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    cost = {start: 0}
    parent = {start: None}
    expanded = 0

    while priority_queue:
        f, current = heapq.heappop(priority_queue)

        expanded += 1

        if current == goal:
            break

        for neighbor in get_neighbors(current):
            new_cost = cost[current] + 1

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                f_cost = new_cost + heuristic(neighbor, goal)

                heapq.heappush(
                    priority_queue,
                    (f_cost, neighbor)
                )

                parent[neighbor] = current

    path = []

    if goal in parent:
        current = goal

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()

    return path, expanded


# BFS Algorithm
def bfs():
    queue = deque([start])
    parent = {start: None}
    expanded = 0

    while queue:
        current = queue.popleft()
        expanded += 1

        if current == goal:
            break

        for neighbor in get_neighbors(current):
            if neighbor not in parent:
                parent[neighbor] = current
                queue.append(neighbor)

    path = []

    if goal in parent:
        current = goal

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()

    return path, expanded


# Run A*
astar_path, astar_nodes = astar()

# Run BFS
bfs_path, bfs_nodes = bfs()


# Display Results
print("----- A* SEARCH -----")
print("Path:", astar_path)
print("Path Cost:", len(astar_path) - 1)
print("Nodes Expanded:", astar_nodes)

print("\n----- BFS SEARCH -----")
print("Path:", bfs_path)
print("Path Cost:", len(bfs_path) - 1)
print("Nodes Expanded:", bfs_nodes)

print("\n----- COMPARISON -----")
print("A* Nodes Expanded :", astar_nodes)
print("BFS Nodes Expanded:", bfs_nodes)
