import unittest

from algorithm.uniformed_search.UCS import uniform_cost_search


class TestUniformCostSearch(unittest.TestCase):
    def test_uniform_cost_search(self):
        # Define a graph represented as adjacency list
        graph = {
            0: [(1, 1), (3, 3)],
            1: [(0, 1), (2, 8)],
            2: [(1, 8), (3, 2)],
            3: [(0, 3), (2, 2)]
        }

        # Test case 1
        start = 0
        end = 1
        result = uniform_cost_search(graph, start, end)
        self.assertEqual(result, [0, 1])

        # Test case 2
        start = 0
        end = 2
        result = uniform_cost_search(graph, start, end)
        self.assertEqual(result, [0, 3, 2])

        # Test case 3 : unreachable node
        graph = {0: [(1, 1)], 1: [(0, 1)]}
        start = 0
        end = 2
        result = uniform_cost_search(graph, start, end)
        self.assertEqual(result, [])

        # Test case 4 : graph with single node
        graph = {0: []}
        start = 0
        end = 0
        result = uniform_cost_search(graph, start, end)
        self.assertEqual(result, [0])


if __name__ == "__main__":
    unittest.main()
