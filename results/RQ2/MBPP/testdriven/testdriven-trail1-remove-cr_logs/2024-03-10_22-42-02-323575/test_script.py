def index_multiplication(test_tup1, test_tup2):
    '''Write a function to perform index wise multiplication of tuple elements in the given two tuples.'''
    
    result = ()
    
    # Error handling for different lengths of input tuples
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples must be of the same length")
    
    for i in range(len(test_tup1)):
        # Perform index-wise multiplication and append the result to the 'result' tuple
        result += (test_tup1[i][0] * test_tup2[i][0], test_tup1[i][1] * test_tup2[i][1]),
    
    return result

assert index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3)) ) == ((6, 21), (12, 45), (2, 9), (7, 30))
import unittest

class Test(unittest.TestCase):
    def test_index_multiplication(self):
        self.assertEqual(index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)),((6, 7), (3, 9), (1, 1), (7, 3))), ((6, 21), (12, 45), (2, 9), (7, 30)))

if __name__ == '__main__':
    unittest.main()