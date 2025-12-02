def sort_matrix(M):
    '''
    Write a function to sort a given matrix in ascending order according to the sum of its rows.
    assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
    '''
    # Sort the matrix M based on the sum of its rows
    sorted_matrix = sorted(M, key=lambda x: sum(x))
    
    return sorted_matrix
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]), [[1, 1, 1], [1, 2, 3], [2, 4, 5]])

if __name__ == '__main__':
    unittest.main()