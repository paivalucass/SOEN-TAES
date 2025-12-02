def count_occurrence(s):
    '''Write a function to count the number of occurrences of the string 'std' in a given string.'''
    return s.count('std')

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_occurance("letstdlenstdporstd"), 3)

if __name__ == '__main__':
    unittest.main()