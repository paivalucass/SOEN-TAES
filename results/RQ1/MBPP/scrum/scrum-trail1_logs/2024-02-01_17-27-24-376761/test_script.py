def Find_Max(lst):
    if lst is None or not isinstance(lst, list):
        return "Error"
    if len(lst) == 0:
        return None
    max_element = max(lst, key=len)
    return max_element
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max([['A'],['A','B'],['A','B','C']]), ['A','B','C'])

if __name__ == '__main__':
    unittest.main()