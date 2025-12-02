def magic_square_test(my_matrix):
    if not my_matrix:
        return False
    n = len(my_matrix)
    if len(my_matrix) != len(my_matrix[0]):
        return False
    s = n*(n**2+1)//2
    sum_rows = [sum(row) for row in my_matrix]
    if not all(sum == s for sum in sum_rows):
        return False
    sum_cols = [sum(col) for col in zip(*my_matrix)]
    if not all(sum == s for sum in sum_cols):
        return False
    sum_diag1 = sum(my_matrix[i][i] for i in range(n))
    if sum_diag1 != s:
        return False
    sum_diag2 = sum(my_matrix[i][n-i-1] for i in range(n))
    if sum_diag2 != s:
        return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_magic_square(self):
        self.assertEqual(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]), True)

if __name__ == '__main__':
    unittest.main()