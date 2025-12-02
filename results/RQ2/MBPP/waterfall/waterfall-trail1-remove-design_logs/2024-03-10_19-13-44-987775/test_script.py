def check_distinct(test_tup):
    if not isinstance(test_tup, tuple):
        raise TypeError("Input must be a tuple")
        
    return len(test_tup) == len(set(test_tup))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_distinct((1, 4, 5, 6, 1, 4)), False)

if __name__ == '__main__':
    unittest.main()