def calculate_row_sum(matrix):
    row_sums = [sum(row) for row in matrix]
    return row_sums

def sort_matrix(matrix):
    row_sums = calculate_row_sum(matrix)
    sorted_matrix = [row for _, row in sorted(zip(row_sums, matrix))]
    return sorted_matrix
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]), [[1, 1, 1], [1, 2, 3], [2, 4, 5]])

if __name__ == '__main__':
    unittest.main()