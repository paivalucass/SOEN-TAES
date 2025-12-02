def find_max(lst):
    if not lst:
        return None
    max_element = max(lst, key=len)
    return max_element
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max([['A'],['A','B'],['A','B','C']]), ['A','B','C'])

if __name__ == '__main__':
    unittest.main()