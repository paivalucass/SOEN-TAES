def check_distinct(test_tup):
    unique_set = set(test_tup)
    return len(unique_set) == len(test_tup)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_distinct((1, 4, 5, 6, 1, 4)), False)

if __name__ == '__main__':
    unittest.main()