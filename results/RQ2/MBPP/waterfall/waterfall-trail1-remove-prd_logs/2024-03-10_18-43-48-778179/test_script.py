def max_of_nth(matrix, n):
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Invalid matrix: All sub-lists must have the same length")
    
    if not 0 < n <= len(matrix[0]):
        raise ValueError("Invalid value of N: Out of range")
    
    return max(row[n-1] for row in matrix) if matrix else None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2), 19)

if __name__ == '__main__':
    unittest.main()