def is_square(matrix):
    n = len(matrix)
    return all(len(row) == n for row in matrix)

def is_magic_square(matrix):
    n = len(matrix)
    sum_diagonal1 = sum(matrix[i][i] for i in range(n))
    sum_diagonal2 = sum(matrix[i][n - i - 1] for i in range(n))
    if sum_diagonal1 != sum_diagonal2:
        return False
    for i in range(n):
        if sum(matrix[i][j] for j in range(n)) != sum_diagonal1:
            return False
        if sum(matrix[j][i] for j in range(n)) != sum_diagonal1:
            return False
    return True

def magic_square_test(my_matrix):
    if not my_matrix or not is_square(my_matrix):
        return False
    return is_magic_square(my_matrix)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]), True)

if __name__ == '__main__':
    unittest.main()