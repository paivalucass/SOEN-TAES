def magic_square_test(my_matrix):
    n = len(my_matrix)
    # Calculate the sum of the first row
    sum_first_row = sum(my_matrix[0])
    # Check if the sum of every row is equal to the sum of the first row
    for i in range(1, n):
        if sum(my_matrix[i]) != sum_first_row:
            return False
    # Check if the sum of every column is equal to the sum of the first row
    for i in range(n):
        col_sum = 0
        for j in range(n):
            col_sum += my_matrix[j][i]
        if col_sum != sum_first_row:
            return False
    # Check if the sum of the main diagonal is equal to the sum of the first row
    diag_sum = 0
    for i in range(n):
        diag_sum += my_matrix[i][i]
    if diag_sum != sum_first_row:
        return False
    # Check if the sum of the secondary diagonal is equal to the sum of the first row
    reverse_diag_sum = 0
    for i in range(n):
        reverse_diag_sum += my_matrix[i][n - i - 1]
    if reverse_diag_sum != sum_first_row:
        return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_magic_square(self):
        self.assertEqual(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]), True)

if __name__ == '__main__':
    unittest.main()