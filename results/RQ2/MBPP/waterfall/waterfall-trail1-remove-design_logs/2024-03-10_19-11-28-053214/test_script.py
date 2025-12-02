def substract_elements(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples must have the same length")
    
    result = tuple(x - y for x, y in zip(test_tup1, test_tup2))
    return result
import unittest

class Test(unittest.TestCase):
    def test_substract_elements(self):
        self.assertEqual(substract_elements((10, 4, 5), (2, 5, 18)), (8, -1, -13))

if __name__ == '__main__':
    unittest.main()