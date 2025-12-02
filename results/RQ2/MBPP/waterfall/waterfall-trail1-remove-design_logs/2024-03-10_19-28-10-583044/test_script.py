def check_smaller(test_tup1, test_tup2):
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Input tuples must have the same length")
    return all(x > y for x, y in zip(test_tup1, test_tup2))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_smaller((1, 2, 3), (2, 3, 4)), False)

if __name__ == '__main__':
    unittest.main()