def list_split(S, step):
    '''Write a function that takes in a list and an integer n and splits a list for every nth element, returning a list of the resulting lists.'''
    result = []
    for i in range(0, len(S), step):
        result.append(S[i:i+step])
    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 3), [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']])

if __name__ == '__main__':
    unittest.main()