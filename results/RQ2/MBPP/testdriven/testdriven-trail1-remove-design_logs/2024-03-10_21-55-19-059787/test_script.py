def sort_matrix(M):
    if not M or not all(isinstance(row, list) for row in M) or not all(all(isinstance(num, int) for num in row) for row in M):
        raise ValueError("Invalid matrix")

    sorted_matrix = sorted(M, key=lambda row: sum(row))
    return sorted_matrix
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]), [[1, 1, 1], [1, 2, 3], [2, 4, 5]])

if __name__ == '__main__':
    unittest.main()