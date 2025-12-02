def sort_matrix(M):
    row_sums = [sum(row) for row in M]
    sorted_indices = sorted(range(len(row_sums)), key=lambda k: row_sums[k])
    sorted_matrix = [M[i] for i in sorted_indices]
    return sorted_matrix
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]), [[1, 1, 1], [1, 2, 3], [2, 4, 5]])

if __name__ == '__main__':
    unittest.main()