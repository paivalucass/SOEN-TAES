def Find_Max(lst):
    max_length = 0
    max_element = []
    for element in lst:
        if len(element) > max_length:
            max_length = len(element)
            max_element = element
    return max_element
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max([['A'],['A','B'],['A','B','C']]), ['A','B','C'])

if __name__ == '__main__':
    unittest.main()