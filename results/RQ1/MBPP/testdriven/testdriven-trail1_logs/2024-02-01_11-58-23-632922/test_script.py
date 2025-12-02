def freq_count(list1):
    '''Write a function to get the frequency of all the elements in a list, returned as a dictionary.'''
    from collections import defaultdict
    freq_dict = defaultdict(int)
    for element in list1:
        freq_dict[element] += 1
    return dict(freq_dict)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(freq_count([10,10,10,10,20,20,20,20,40,40,50,50,30]), {10: 4, 20: 4, 40: 2, 50: 2, 30: 1})

if __name__ == '__main__':
    unittest.main()