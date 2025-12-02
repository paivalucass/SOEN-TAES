def magic_square_test(my_matrix):
    if not isinstance(my_matrix, list) or len(my_matrix) == 0:
        return "Invalid Input"

    n = len(my_matrix)
    if any(len(row) != n for row in my_matrix):
        return "Invalid Input"

    if any(any(not isinstance(cell, int) for cell in row) for row in my_matrix):
        return "Invalid Input"

    magic_sum = n * (n**2 + 1) // 2

    # Check rows and columns
    if any(sum(row) != magic_sum for row in my_matrix) or any(sum(row[i] for row in my_matrix) != magic_sum for i in range(n)):
        return False

    # Check diagonals
    if sum(my_matrix[i][i] for i in range(n)) != magic_sum or sum(my_matrix[i][n-i-1] for i in range(n)) != magic_sum:
        return False

    return True
import unittest

class Test(unittest.TestCase):
    def test_magic_square(self):
        self.assertEqual(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]), True)

if __name__ == '__main__':
    unittest.main()