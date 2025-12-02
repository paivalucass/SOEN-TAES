def magic_square_test(my_matrix):
    if len(my_matrix) != len(my_matrix[0]):
        raise ValueError("Input matrix is not a square matrix")
    
    total = sum(my_matrix[0])
    row_sums = [sum(row) for row in my_matrix]
    col_sums = [sum(col) for col in zip(*my_matrix)]
    diag_sum1 = sum(my_matrix[i][i] for i in range(len(my_matrix)))
    diag_sum2 = sum(my_matrix[i][len(my_matrix)-1-i] for i in range(len(my_matrix)))
    if all(val == total for val in row_sums) and all(val == total for val in col_sums) and diag_sum1 == total and diag_sum2 == total:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test_magic_square(self):
        self.assertEqual(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]), True)

if __name__ == '__main__':
    unittest.main()