import unittest

from algorithm.uniformed_search.BFS_shortest_path import bread_first_search


class TestBFSShortestPath(unittest.TestCase):
    def setUp(self):
        self.graph = {
            1: [(2, 1), (3, 1)],
            2: [(1, 1), (4, 1)],
            3: [(1, 1), (4, 1), (5, 1)],
            4: [(2, 1), (3, 1), (5, 1)],
            5: [(3, 1), (4, 1)]
        }

    def test_shortest_path_found(self):
        start, target = 1, 5
        expected_path = [1, 3, 5]
        actual_path = bread_first_search(self.graph, start, target)

        self.assertEqual(expected_path, actual_path)

    def test_shortest_path_not_found(self):
        start, target = 1, 6  # 6 is not in graph's vertices
        expected_path = []
        actual_path = bread_first_search(self.graph, start, target)

        self.assertEqual(expected_path, actual_path)

    def test_shortest_path_same_start_and_target(self):
        start, target = 1, 1
        expected_path = [1]
        actual_path = bread_first_search(self.graph, start, target)

        self.assertEqual(expected_path, actual_path)


if __name__ == "__main__":
    unittest.main()
