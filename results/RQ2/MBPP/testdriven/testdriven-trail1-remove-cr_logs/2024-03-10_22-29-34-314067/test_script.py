from collections import Counter

def freq_count(list1):
    '''Write a function to get the frequency of all the elements in a list, returned as a dictionary.'''
    counter = Counter(list1)
    frequency_dict = dict(counter)
    
    return frequency_dict

import unittest

class Test(unittest.TestCase):
    def test_freq_count(self):
        self.assertEqual(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]), {10: 4, 20: 4, 40: 2, 50: 2, 30: 1})

if __name__ == '__main__':
    unittest.main()