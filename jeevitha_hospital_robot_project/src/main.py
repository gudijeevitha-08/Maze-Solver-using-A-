"""Run the A* vs BFS demo and the hospital delivery planner."""
from maze import astar, bfs, render_maze
from hospital_planner import schedule_deliveries, plan_delivery_route

MAZE = [
    [0,0,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,0,0,0,0,1,0],
    [0,1,1,1,0,1,0],
    [0,0,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,0,0,0,0,0,0],
]
START, GOAL = (0, 0), (6, 6)

def main():
    print("=== PHASE 1: MAZE SOLVER ===")
    print("Original maze (# wall, . free, S start, G goal):")
    print(render_maze(MAZE, start=START, goal=GOAL))
    for name, solver in [("BFS", bfs), ("A*", astar)]:
        path, expanded, cost = solver(MAZE, START, GOAL)
        print(f"\n{name} result")
        print(render_maze(MAZE, path, START, GOAL))
        print(f"Path found: {bool(path)} | Path steps: {cost} | Nodes expanded: {expanded}")

    print("\n=== PHASE 2: HOSPITAL DELIVERY PLANNER ===")
    tasks = ["Medicine-ICU", "Sample-Lab", "Medicine-Ward"]
    allowed_slots = {
        "Medicine-ICU": ["09:00", "10:00"],
        "Sample-Lab": ["09:00", "10:00", "11:00"],
        "Medicine-Ward": ["10:00", "11:00"],
    }
    # Tasks share one robot, so these deliveries cannot occur in the same slot.
    schedule = schedule_deliveries(tasks, allowed_slots,
                                  constraints=[("Medicine-ICU", "Sample-Lab"),
                                               ("Medicine-ICU", "Medicine-Ward"),
                                               ("Sample-Lab", "Medicine-Ward")])
    print("Delivery schedule (CSP + MRV + AC-3):")
    print(schedule if schedule else "No feasible schedule")

    busy = [(2, 2)]
    result = plan_delivery_route(MAZE, START, GOAL, busy_cells=busy)
    print("\nRoute with dynamic obstacle:")
    print(render_maze(result["grid"], result["path"], START, GOAL))
    print(f"Path steps: {result['cost']} | Nodes expanded: {result['nodes_expanded']}")
    print("Explanation:")
    for note in result["explanations"]:
        print("-", note)
    if not result["path"]:
        print("No route exists with current obstacles; request human intervention.")

if __name__ == "__main__":
    main()
