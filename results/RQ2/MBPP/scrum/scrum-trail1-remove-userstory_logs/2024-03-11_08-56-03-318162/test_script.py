def magic_square_test(my_matrix):
    # Implement the logic to check if the given matrix is a magic square
    # Include the algorithm to verify if the sum of rows, columns, and diagonals is equal
    
    # Write test cases to cover different scenarios such as a valid magic square, an invalid magic square, 
    # and edge cases like an empty matrix
    # Test the code with both odd and even order matrices
    
    n = len(my_matrix)
    magic_sum = n * (n**2 + 1) / 2

    # Check if the matrix is a square
    if not all(len(row) == n for row in my_matrix):
        return False
    
    # Check for non-numeric values
    if not all(isinstance(cell, int) for row in my_matrix for cell in row):
        return False
    
    # Check for duplicate numbers
    flat_matrix = [cell for row in my_matrix for cell in row]
    if len(flat_matrix) != len(set(flat_matrix)):
        return False
    
    # Check if the sum of rows, columns, and diagonals is equal to magic_sum
    row_sums = [sum(row) for row in my_matrix]
    col_sums = [sum(my_matrix[i][j] for i in range(n)) for j in range(n)]
    diag1_sum = sum(my_matrix[i][i] for i in range(n))
    diag2_sum = sum(my_matrix[i][n-1-i] for i in range(n))
    
    if (all(sum == magic_sum for sum in row_sums) and
        all(sum == magic_sum for sum in col_sums) and
        diag1_sum == magic_sum and diag2_sum == magic_sum):
        return True
    else:
        return False

# Test cases
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]) == True
assert magic_square_test([[7, 12, 1], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]) == False
assert magic_square_test([[7, '12', 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]) == False
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 9, 4]]) == False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]), True)

if __name__ == '__main__':
    unittest.main()