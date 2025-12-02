def Find_Max(lst):
    if not isinstance(lst, list):
        raise TypeError("Input should be a list")
    if not lst:
        return None
    max_length_element = max(lst, key=len)
    return max_length_element
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max([['A'],['A','B'],['A','B','C']]), ['A','B','C'])

if __name__ == '__main__':
    unittest.main()