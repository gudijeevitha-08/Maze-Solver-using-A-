import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from maze import astar, bfs, manhattan
from hospital_planner import schedule_deliveries, plan_delivery_route

class ProjectTests(unittest.TestCase):
    def setUp(self):
        self.grid = [[0,0,0],[1,1,0],[0,0,0]]
    def test_manhattan(self):
        self.assertEqual(manhattan((0,0), (2,2)), 4)
    def test_astar_and_bfs_optimal_cost(self):
        a_path, _, a_cost = astar(self.grid, (0,0), (2,2))
        b_path, _, b_cost = bfs(self.grid, (0,0), (2,2))
        self.assertTrue(a_path)
        self.assertEqual(a_cost, b_cost)
    def test_csp_no_conflict(self):
        tasks = ["A", "B"]
        slots = {"A": ["9", "10"], "B": ["9", "10"]}
        answer = schedule_deliveries(tasks, slots, [("A", "B")])
        self.assertIsNotNone(answer)
        self.assertNotEqual(answer["A"], answer["B"])
    def test_route_dynamic_obstacle(self):
        result = plan_delivery_route(self.grid, (0,0), (2,2), blocked_cells=[(2,1)])
        self.assertTrue(result["path"])
        self.assertNotIn((2,1), result["path"])

if __name__ == "__main__":
    unittest.main()
