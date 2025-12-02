def sort_matrix(M):
    if not M or len(M) == 1:
        raise ValueError("Invalid input: Matrix must have at least two rows")
    
    row_sums = [sum(row) for row in M]
    sorted_matrix = [row for _, row in sorted(zip(row_sums, M))]
    
    return sorted_matrix
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]), [[1, 1, 1], [1, 2, 3], [2, 4, 5]])

if __name__ == '__main__':
    unittest.main()