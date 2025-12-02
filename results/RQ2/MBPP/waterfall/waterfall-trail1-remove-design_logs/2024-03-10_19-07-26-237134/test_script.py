def is_magic_square(matrix):
    size = len(matrix)
    primary_diag_sum = sum(matrix[i][i] for i in range(size))
    secondary_diag_sum = sum(matrix[i][size-1-i] for i in range(size))
    
    if primary_diag_sum != secondary_diag_sum:
        return False
    
    for i in range(size):
        if (sum(matrix[i][j] for j in range(size)) != primary_diag_sum) or (sum(matrix[j][i] for j in range(size)) != primary_diag_sum):
            return False
    
    return True

def magic_square_test(my_matrix):
    size = len(my_matrix)
    primary_diag_sum = sum(my_matrix[i][i] for i in range(size))
    secondary_diag_sum = sum(my_matrix[i][size-1-i] for i in range(size))
    
    if primary_diag_sum != secondary_diag_sum:
        return False
    
    for i in range(size):
        if (sum(my_matrix[i][j] for j in range(size)) != primary_diag_sum) or (sum(my_matrix[j][i] for j in range(size)) != primary_diag_sum):
            return False
    
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]), True)

if __name__ == '__main__':
    unittest.main()