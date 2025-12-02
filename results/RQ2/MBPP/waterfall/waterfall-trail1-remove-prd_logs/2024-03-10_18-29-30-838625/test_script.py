def magic_square_test(matrix):
    if not matrix or len(matrix) != len(matrix[0]):
        return False

    if not check_row_sum(matrix):
        return False

    if not check_column_sum(matrix):
        return False

    if not check_diagonal_sum(matrix):
        return False

    return True

def check_row_sum(matrix):
    target_sum = sum(matrix[0])
    for row in matrix:
        if sum(row) != target_sum:
            return False
    return True

def check_column_sum(matrix):
    n = len(matrix)
    target_sum = sum(matrix[0])
    for i in range(n):
        col_sum = 0
        for j in range(n):
            col_sum += matrix[j][i]
        if col_sum != target_sum:
            return False
    return True

def check_diagonal_sum(matrix):
    n = len(matrix)
    target_sum = sum(matrix[0])
    diag_sum1 = 0
    diag_sum2 = 0
    for i in range(n):
        diag_sum1 += matrix[i][i]
        diag_sum2 += matrix[i][n-1-i]
    if diag_sum1 != target_sum or diag_sum2 != target_sum:
        return False
    return True

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]), True)

if __name__ == '__main__':
    unittest.main()