def maximize_elements(test_tup1, test_tup2):
    if not isinstance(test_tup1, tuple) or not isinstance(test_tup2, tuple):
        raise TypeError("Input parameters must be tuples")
    
    if not test_tup1 or not test_tup2:
        return ()
    
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples have different lengths")
    
    result = tuple(max(a, b) for a, b in zip(test_tup1, test_tup2))
    return result

import unittest

class Test(unittest.TestCase):
    def test_maximize_elements(self):
        self.assertEqual(maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))), ((6, 7), (4, 9), (2, 9), (7, 10)))

if __name__ == '__main__':
    unittest.main()