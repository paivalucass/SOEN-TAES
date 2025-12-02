def magic_square_test(my_matrix):
    n = len(my_matrix)
    sum_rows = [sum(row) for row in my_matrix]
    sum_columns = [sum(my_matrix[i][j] for i in range(n)) for j in range(n)]
    sum_diagonals = [sum(my_matrix[i][i] for i in range(n)), sum(my_matrix[i][n-1-i] for i in range(n))]
    if len(set(sum_rows + sum_columns + sum_diagonals)) == 1:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]), True)

if __name__ == '__main__':
    unittest.main()