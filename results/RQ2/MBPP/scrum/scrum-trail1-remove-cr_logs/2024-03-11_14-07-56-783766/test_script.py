def check_smaller(test_tup1, test_tup2):
    if not test_tup1 or not test_tup2:
        raise ValueError("Input tuples cannot be empty")
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples must be of the same length")
    for i in range(len(test_tup1)):
        if not isinstance(test_tup1[i], (int, float)) or not isinstance(test_tup2[i], (int, float)):
            raise TypeError("Input tuples must contain only numbers")
    result = all(test_tup2[i] < test_tup1[i] for i in range(len(test_tup1)))
    return result
import unittest

class Test(unittest.TestCase):
    def test_check_smaller(self):
        self.assertEqual(check_smaller((1, 2, 3), (2, 3, 4)), False)

if __name__ == '__main__':
    unittest.main()