def magic_square_test(my_matrix):
    n = len(my_matrix)
    sum_diag1 = sum(my_matrix[i][i] for i in range(n))
    sum_diag2 = sum(my_matrix[i][n-1-i] for i in range(n))
    if sum_diag1 != sum_diag2:
        return False
    for i in range(n):
        if sum(my_matrix[i][j] for j in range(n)) != sum_diag1 or sum(my_matrix[j][i] for j in range(n)) != sum_diag1:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_magic_square(self):
        self.assertEqual(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]), True)

if __name__ == '__main__':
    unittest.main()