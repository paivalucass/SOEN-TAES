def magic_square_test(my_matrix):
    if not isinstance(my_matrix, list) or len(my_matrix) == 0:
        return False
    n = len(my_matrix)
    magic_sum = sum(my_matrix[0]) 
    for row in my_matrix:
        if len(row) != n or not all(isinstance(element, int) for element in row):
            return False
        if sum(row) != magic_sum:
            return False
    for i in range(n):
        col_sum = sum(my_matrix[j][i] for j in range(n))
        if col_sum != magic_sum:
            return False
    diag_sum1 = sum(my_matrix[i][i] for i in range(n))
    diag_sum2 = sum(my_matrix[i][n-1-i] for i in range(n))
    if diag_sum1 != magic_sum or diag_sum2 != magic_sum:
        return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_magic_square(self):
        self.assertEqual(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]), True)

if __name__ == '__main__':
    unittest.main()