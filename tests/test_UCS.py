import heapq
import unittest

from algorithm.uniformed_search.UCS import uniform_cost_search


class TestUniformCostSearch(unittest.TestCase):

    def setUp(self):
        self.simple_graph = {0: [(1, 1), (2, 5)], 1: [(2, 2)], 2: []}

    def test_uniform_cost_search_basic(self):
        result = uniform_cost_search(self.simple_graph, 0, 2)
        self.assertEqual(result, [0, 1, 2])

    def test_uniform_cost_search_same_start_goal(self):
        result = uniform_cost_search(self.simple_graph, 1, 1)
        self.assertEqual(result, [1])

    def test_uniform_cost_search_unreachable_goal(self):
        result = uniform_cost_search(self.simple_graph, 0, 3)
        self.assertEqual(result, [])

    def test_uniform_cost_search_empty_graph(self):
        result = uniform_cost_search({}, 0, 1)
        self.assertEqual(result, [])

    def test_uniform_cost_search_nonexisting_start(self):
        result = uniform_cost_search(self.simple_graph, 4, 2)
        self.assertEqual(result, [])

    def test_uniform_cost_search_nonexisting_goal(self):
        result = uniform_cost_search(self.simple_graph, 0, 5)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
