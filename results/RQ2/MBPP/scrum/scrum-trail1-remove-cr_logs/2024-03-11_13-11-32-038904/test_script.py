def check_distinct(test_tup):
    distinct_set = set(test_tup)
    if len(distinct_set) == len(test_tup):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_distinct((1, 4, 5, 6, 1, 4)), False)

if __name__ == '__main__':
    unittest.main()