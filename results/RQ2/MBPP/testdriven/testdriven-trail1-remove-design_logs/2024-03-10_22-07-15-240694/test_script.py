def Find_Max(lst):
    if not isinstance(lst, list) or not lst:
        return "Error: Input is not a non-empty list"
    max_element = max(lst, key=len)
    return max_element
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max([['A'],['A','B'],['A','B','C']]), ['A','B','C'])

if __name__ == '__main__':
    unittest.main()