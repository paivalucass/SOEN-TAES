def sort_matrix(M):
    '''
    Write a function to sort a given matrix in ascending order according to the sum of its rows.
    assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
    '''

    # Calculate the sum of each row in the matrix
    row_sums = [sum(row) for row in M]

    # Sort the indices of the rows based on their sums
    sorted_indices = sorted(range(len(M)), key=lambda i: row_sums[i])

    # Create a new matrix with rows sorted based on their sums
    sorted_matrix = [M[i] for i in sorted_indices]

    return sorted_matrix
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]), [[1, 1, 1], [1, 2, 3], [2, 4, 5]])

if __name__ == '__main__':
    unittest.main()