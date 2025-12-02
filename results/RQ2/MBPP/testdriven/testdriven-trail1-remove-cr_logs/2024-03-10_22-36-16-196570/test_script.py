def subtract_elements(test_tup1, test_tup2):
    if not all(isinstance(i, (int, float)) for i in test_tup1) or not all(isinstance(i, (int, float)) for i in test_tup2):
        return "Error: Input tuples must contain only numeric values"
    result = tuple(a - b for a, b in zip(test_tup1, test_tup2))
    return result
import unittest

class Test(unittest.TestCase):
    def test_substract_elements(self):
        self.assertEqual(substract_elements((10, 4, 5), (2, 5, 18)), (8, -1, -13))

if __name__ == '__main__':
    unittest.main()