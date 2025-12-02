def Find_Max(lst):
    if not lst:
        return "Error/Exception"

    max_element = max(lst, key=len)
    return max_element
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max([['A'],['A','B'],['A','B','C']]), ['A','B','C'])

if __name__ == '__main__':
    unittest.main()