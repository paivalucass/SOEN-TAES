def find_max_element(lst):
    if not lst or not all(isinstance(element, list) for element in lst):
        raise ValueError("Input list is either empty or contains non-list elements")

    max_element = max(lst, key=len)
    return max_element
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Find_Max([['A'],['A','B'],['A','B','C']]), ['A','B','C'])

if __name__ == '__main__':
    unittest.main()