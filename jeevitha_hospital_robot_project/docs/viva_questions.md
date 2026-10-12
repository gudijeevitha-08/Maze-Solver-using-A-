# Viva Preparation

1. **What is A*?** An informed search algorithm that prioritises nodes using f(n)=g(n)+h(n).
2. **What is Manhattan distance?** |row difference| + |column difference|; suitable for four-direction unit-cost grids.
3. **Why compare BFS and A*?** BFS has no heuristic; A* uses goal-distance estimates. Compare path cost and expanded nodes on the same maze.
4. **What is a CSP?** A problem defined by variables, domains and constraints.
5. **What is MRV?** Minimum Remaining Values selects the unassigned variable with the fewest legal values.
6. **What does AC-3 do?** Removes domain values that have no supporting value in a neighbouring variable's domain.
7. **Why replan?** A busy or blocked cell changes the traversable map; A* is run again on the updated map.
8. **What are limitations?** Manual obstacle input, small demo, simplified rules; not safe for real clinical use without validation and human oversight.
