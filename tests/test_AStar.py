import heapq
import unittest

from algorithm.informed_search.AStar import AStar


class TestAStar(unittest.TestCase):

    def setUp(self):
        self.graph = {1: [(2, 2), (3, 5)], 2: [(4, 1)], 3: [], 4: []}
        self.start = 1
        self.goal = 4
        self.heuristic = {1: 0, 2: 1, 3: 5, 4: 6}

    def test_AStar_valid(self):
        expected_result = [1, 2, 4]
        self.assertEqual(AStar(self.graph, self.start, self.goal, self.heuristic), expected_result, "Valid Case")

    def test_AStar_goal_is_start(self):
        expected_result = [1]
        self.assertEqual(AStar(self.graph, self.start, self.start, self.heuristic), expected_result, "Start is Goal")

    def test_AStar_unreachable_goal(self):
        expected_result = []
        self.assertEqual(AStar(self.graph, self.start, 999, self.heuristic), expected_result, "Unreachable Goal")

    def test_AStar_empty_graph(self):
        expected_result = []
        self.assertEqual(AStar({}, self.start, self.goal, self.heuristic), expected_result, "Empty graph")

    def test_AStar_no_heuristics(self):
        expected_result = []
        self.assertEqual(AStar(self.graph, self.start, self.goal, {}), expected_result, "No Heuristics")

    def tearDown(self):
        self.graph = None
        self.start = None
        self.goal = None
        self.heuristic = None


if __name__ == '__main__':
    unittest.main()
