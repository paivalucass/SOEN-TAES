def sort_matrix(M):
    if not M or not all(len(row) == len(M[0]) for row in M):
        raise ValueError("Input matrix is empty or has invalid dimensions")
    
    sorted_matrix = sorted(M, key=lambda row: sum(row))
    return sorted_matrix
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]), [[1, 1, 1], [1, 2, 3], [2, 4, 5]])

if __name__ == '__main__':
    unittest.main()