def index_multiplication(test_tup1, test_tup2):
    # Input validation
    for tup in (test_tup1, test_tup2):
        if not all(isinstance(x, (int, float)) for sub_tup in tup for x in sub_tup):
            raise ValueError("Input tuples should contain only numeric elements")
        if len(tup) != len(test_tup1):
            raise ValueError("Input tuples should have the same length")
    
    # Perform index-wise multiplication
    result_tup = tuple((x1 * x2, y1 * y2) for (x1, y1), (x2, y2) in zip(test_tup1, test_tup2))
    return result_tup

import unittest

class Test(unittest.TestCase):
    def test_index_multiplication(self):
        self.assertEqual(index_multiplication(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))), 
                         ((6, 21), (12, 45), (2, 9), (7, 30)))

if __name__ == '__main__':
    unittest.main()