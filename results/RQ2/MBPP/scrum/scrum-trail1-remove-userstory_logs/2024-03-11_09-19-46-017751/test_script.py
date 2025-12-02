def max_of_nth(matrix, N):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise ValueError("Input matrix should be a list of lists")

    if not 0 <= N < len(matrix[0]):
        raise ValueError("N is out of range for the matrix columns")

    max_val = float('-inf')
    for row in matrix:
        if len(row) <= N:
            raise ValueError("N is out of range for the row length")
        max_val = max(max_val, row[N])

    return max_val
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2), 19)

if __name__ == '__main__':
    unittest.main()