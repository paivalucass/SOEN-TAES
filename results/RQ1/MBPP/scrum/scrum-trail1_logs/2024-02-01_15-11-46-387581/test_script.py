def count_first_elements(test_tup, elem):
    '''Write a function to find the number of elements that occurs before the tuple element in the given tuple.'''
    count = 0
    for item in test_tup:
        if item == elem:
            break
        count += 1
    return count

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_first_elements((1, 5, 7, (4, 6), 10)), 3)

if __name__ == '__main__':
    unittest.main()