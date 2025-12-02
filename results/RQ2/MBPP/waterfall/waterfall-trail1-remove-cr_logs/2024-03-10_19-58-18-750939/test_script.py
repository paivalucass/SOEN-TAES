def maximize_elements(test_tup1, test_tup2):
    if not isinstance(test_tup1, tuple) or not isinstance(test_tup2, tuple):
        raise TypeError("Input parameters must be tuples")
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples must have the same length")
    
    result_tup = tuple((max(test_tup1[i][0], test_tup2[i][0]), max(test_tup1[i][1], test_tup2[i][1])) for i in range(len(test_tup1)))
    
    return result_tup

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))), ((6, 7), (4, 9), (2, 9), (7, 10)))

if __name__ == '__main__':
    unittest.main()