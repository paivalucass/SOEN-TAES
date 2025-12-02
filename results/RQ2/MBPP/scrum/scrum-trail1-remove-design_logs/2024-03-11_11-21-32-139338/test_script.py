def check_smaller(test_tup1, test_tup2):
    return all(x > y for x, y in zip(test_tup1, test_tup2))
import unittest

class Test(unittest.TestCase):
    def test_check_smaller(self):
        self.assertEqual(check_smaller((1, 2, 3), (2, 3, 4)), False)

if __name__ == '__main__':
    unittest.main()