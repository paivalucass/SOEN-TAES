def magic_square_test(my_matrix):
    '''
    Write a function to calculate whether the matrix is a magic square.
    assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
    '''
    if not my_matrix:
        return False

    n = len(my_matrix)

    # Check if the input matrix is a square
    for row in my_matrix:
        if len(row) != n:
            return "InvalidInputError"
    
    target_sum = sum(my_matrix[0])  # Calculate the sum of the first row

    # Check rows and columns
    for i in range(n):
        if sum(my_matrix[i]) != target_sum:  # Check row sum
            return False

        # Calculate column sum
        col_sum = 0
        for j in range(n):
            col_sum += my_matrix[j][i]
        if col_sum != target_sum:
            return False

    # Check diagonals
    diag_sum1 = sum(my_matrix[i][i] for i in range(n))
    diag_sum2 = sum(my_matrix[i][n-1-i] for i in range(n))
    if diag_sum1 != target_sum or diag_sum2 != target_sum:
        return False

    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]), True)

if __name__ == '__main__':
    unittest.main()