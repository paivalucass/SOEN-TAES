def common_element(list1, list2):
    '''Write a function that takes two lists and returns true if they have at least one common element.'''
    for element in list1:
        if element in list2:
            return True
    return False

assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(common_element([1,2,3,4,5], [5,6,7,8,9]), True)

if __name__ == '__main__':
    unittest.main()