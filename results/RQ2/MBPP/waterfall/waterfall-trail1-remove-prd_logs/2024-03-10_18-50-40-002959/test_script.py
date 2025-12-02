def check_smaller(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples must have the same length")

    if not all(isinstance(x, (int, float)) for x in test_tup1) or not all(isinstance(x, (int, float)) for x in test_tup2):
        raise ValueError("Input tuples must contain only numeric elements")

    for i in range(len(test_tup1)):
        if test_tup2[i] >= test_tup1[i]:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_check_smaller(self):
        self.assertEqual(check_smaller((1, 2, 3), (2, 3, 4)), False)

if __name__ == '__main__':
    unittest.main()