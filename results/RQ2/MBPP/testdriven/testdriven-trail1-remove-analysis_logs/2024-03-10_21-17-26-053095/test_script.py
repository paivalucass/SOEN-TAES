def check_distinct(test_tup):
    '''Write a function to check if given tuple contains no duplicates.
    assert check_distinct((1, 4, 5, 6, 1, 4)) == False'''
    seen_values = set()
    for element in test_tup:
        if element in seen_values:
            return False
        else:
            seen_values.add(element)
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_distinct((1, 4, 5, 6, 1, 4)), False)

if __name__ == '__main__':
    unittest.main()