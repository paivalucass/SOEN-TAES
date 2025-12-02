def division_elements(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples must be of the same length")
    if not all(isinstance(num, (int, float)) for num in test_tup1) or not all(isinstance(num, (int, float)) for num in test_tup2):
        raise ValueError("Input tuples must contain only numeric values")
    
    result = [a / b for a, b in zip(test_tup1, test_tup2)]
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(division_elements((10, 4, 6, 9), (5, 2, 3, 3)), (2, 2, 2, 3))

if __name__ == '__main__':
    unittest.main()