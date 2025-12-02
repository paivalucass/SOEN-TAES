def common_element(list1: list, list2: list) -> bool:
    '''Write a function that takes two lists and returns true if they have at least one common element.'''
    return any(item in list2 for item in list1)
import unittest

class Test(unittest.TestCase):
    def test_common_element(self):
        self.assertEqual(common_element([1,2,3,4,5], [5,6,7,8,9]), True)

if __name__ == '__main__':
    unittest.main()