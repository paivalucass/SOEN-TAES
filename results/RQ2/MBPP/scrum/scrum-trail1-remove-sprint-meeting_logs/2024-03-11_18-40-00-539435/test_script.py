def check_distinct(test_tup):
    '''Write a function to check if given tuple contains no duplicates.'''
    distinct_elements = set(test_tup)
    if len(distinct_elements) == len(test_tup):
        return True
    else:
        return False

assert check_distinct((1, 4, 5, 6, 1, 4)) == False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_distinct((1, 4, 5, 6, 1, 4)), False)

if __name__ == '__main__':
    unittest.main()