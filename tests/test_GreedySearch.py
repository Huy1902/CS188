import heapq
import unittest

from algorithm.informed_search.GreedySearch import GreedySearch


class TestGreedySearch(unittest.TestCase):

    def test_basic(self):
        graph = {0: [1, 2, 3], 1: [0, 4, 5], 2: [0], 3: [0], 4: [1], 5: [1]}
        start = 0
        goal = 5
        heuristic = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1, 5: 0}

        expected_result = [0, 1, 5]

        self.assertListEqual(GreedySearch(graph, start, goal, heuristic), expected_result)

    def test_empty_graph(self):
        graph = {}
        start = 1
        goal = 2
        heuristic = {}

        expected_result = []

        self.assertListEqual(GreedySearch(graph, start, goal, heuristic), expected_result)

    def test_no_path(self):
        graph = {1: [2], 2: [3], 3: [4]}
        start = 1
        goal = 5
        heuristic = {1: 4, 2: 3, 3: 2, 4: 1, 5: 0}

        expected_result = []

        self.assertListEqual(GreedySearch(graph, start, goal, heuristic), expected_result)


if __name__ == "__main__":
    unittest.main()
