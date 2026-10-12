"""Small educational CSP scheduler and rule-based dynamic route planner."""
from itertools import product
from maze import astar

def revise(domains, xi, xj, compatible):
    """AC-3 revise: remove values in xi with no supporting value in xj."""
    revised = False
    for x in list(domains[xi]):
        if not any(compatible(x, y) for y in domains[xj]):
            domains[xi].remove(x)
            revised = True
    return revised

def ac3(domains, arcs, compatible):
    """Run AC-3 on a copied domains dictionary; return None on inconsistency."""
    domains = {k: list(v) for k, v in domains.items()}
    queue = list(arcs)
    while queue:
        xi, xj = queue.pop(0)
        if revise(domains, xi, xj, compatible):
            if not domains[xi]:
                return None
            for xk in domains:
                if xk != xi and xk != xj:
                    queue.append((xk, xi))
    return domains

def schedule_deliveries(tasks, slots, constraints=None):
    """
    CSP: tasks are delivery IDs; each task has a list of allowed time slots.
    Constraints are pairs of tasks that must not share a slot.
    Returns a schedule dictionary or None.
    """
    constraints = set(tuple(sorted(pair)) for pair in (constraints or []))
    domains = {t: list(slots[t]) for t in tasks}

    def compatible(x, y):
        return x != y

    arcs = [(a, b) for a, b in constraints] + [(b, a) for a, b in constraints]
    propagated = ac3(domains, arcs, compatible)
    if propagated is None:
        return None

    def consistent(task, slot, assignment):
        for other, other_slot in assignment.items():
            if tuple(sorted((task, other))) in constraints and slot == other_slot:
                return False
        return True

    def backtrack(assignment, current_domains):
        if len(assignment) == len(tasks):
            return dict(assignment)
        unassigned = [t for t in tasks if t not in assignment]
        # MRV: choose task with the fewest remaining legal values.
        task = min(unassigned, key=lambda t: sum(
            consistent(t, v, assignment) for v in current_domains[t]))
        values = sorted(current_domains[task])
        for value in values:
            if not consistent(task, value, assignment):
                continue
            assignment[task] = value
            reduced = {k: list(v) for k, v in current_domains.items()}
            for other in unassigned:
                if other != task and tuple(sorted((task, other))) in constraints:
                    reduced[other] = [v for v in reduced[other] if v != value]
            if all(reduced[t] for t in tasks if t not in assignment):
                result = backtrack(assignment, reduced)
                if result is not None:
                    return result
            del assignment[task]
        return None

    return backtrack({}, propagated)

def apply_hospital_rules(grid, busy_cells=(), blocked_cells=()):
    """
    Rule examples:
    Zone(cell, ICU) -> RequiresSterile(robot) (reported as a safety note).
    Corridor(cell) AND Busy(cell, time) -> AvoidOrSlow(cell).
    Busy/blocked cells are temporarily treated as obstacles in this demo.
    """
    updated = [row[:] for row in grid]
    notes = []
    for cell in set(busy_cells) | set(blocked_cells):
        r, c = cell
        if 0 <= r < len(updated) and 0 <= c < len(updated[0]):
            updated[r][c] = 1
            notes.append(f"Rule fired: cell {cell} is busy/blocked; route planner avoids it.")
    notes.append("Safety rule: deliveries entering ICU zones require a sterile robot.")
    return updated, notes

def plan_delivery_route(grid, start, goal, busy_cells=(), blocked_cells=()):
    updated, notes = apply_hospital_rules(grid, busy_cells, blocked_cells)
    path, expanded, cost = astar(updated, start, goal)
    return {"path": path, "nodes_expanded": expanded, "cost": cost,
            "grid": updated, "explanations": notes}
