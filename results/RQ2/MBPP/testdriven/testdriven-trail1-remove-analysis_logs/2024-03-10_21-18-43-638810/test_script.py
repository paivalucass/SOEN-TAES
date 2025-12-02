def Find_Max(lst): 
    if not isinstance(lst, list) or not all(isinstance(item, list) for item in lst):
        return "Input should be a list of lists"

    if not lst:
        return None

    max_list = max(lst, key=len)
    return max_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max([['A'],['A','B'],['A','B','C']]), ['A','B','C'])

if __name__ == '__main__':
    unittest.main()