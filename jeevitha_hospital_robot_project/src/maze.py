"""Grid maze helpers. 0 = free cell, 1 = wall."""
from collections import deque
import heapq

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def valid_neighbors(grid, cell):
    rows, cols = len(grid), len(grid[0])
    for dr, dc in DIRECTIONS:
        nxt = (cell[0] + dr, cell[1] + dc)
        if 0 <= nxt[0] < rows and 0 <= nxt[1] < cols and grid[nxt[0]][nxt[1]] == 0:
            yield nxt

def reconstruct_path(parent, goal):
    if goal not in parent:
        return []
    path, cur = [], goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    return list(reversed(path))

def astar(grid, start, goal):
    """Return (path, nodes_expanded, cost). Each move costs 1."""
    frontier = [(manhattan(start, goal), 0, start)]
    parent, g_cost = {start: None}, {start: 0}
    closed, expanded = set(), 0
    while frontier:
        _, g, current = heapq.heappop(frontier)
        if current in closed or g != g_cost.get(current):
            continue
        if current == goal:
            return reconstruct_path(parent, goal), expanded, g
        closed.add(current)
        expanded += 1
        for nxt in valid_neighbors(grid, current):
            new_g = g + 1
            if new_g < g_cost.get(nxt, float("inf")):
                g_cost[nxt] = new_g
                parent[nxt] = current
                heapq.heappush(frontier, (new_g + manhattan(nxt, goal), new_g, nxt))
    return [], expanded, None

def bfs(grid, start, goal):
    """Return (path, nodes_expanded, cost). Each move costs 1."""
    q = deque([start])
    parent, distance = {start: None}, {start: 0}
    expanded = 0
    while q:
        current = q.popleft()
        if current == goal:
            return reconstruct_path(parent, goal), expanded, distance[current]
        expanded += 1
        for nxt in valid_neighbors(grid, current):
            if nxt not in parent:
                parent[nxt] = current
                distance[nxt] = distance[current] + 1
                q.append(nxt)
    return [], expanded, None

def render_maze(grid, path=(), start=None, goal=None):
    path = set(path)
    lines = []
    for r, row in enumerate(grid):
        chars = []
        for c, value in enumerate(row):
            cell = (r, c)
            if cell == start: ch = "S"
            elif cell == goal: ch = "G"
            elif value == 1: ch = "#"
            elif cell in path: ch = "*"
            else: ch = "."
            chars.append(ch)
        lines.append(" ".join(chars))
    return "\n".join(lines)
