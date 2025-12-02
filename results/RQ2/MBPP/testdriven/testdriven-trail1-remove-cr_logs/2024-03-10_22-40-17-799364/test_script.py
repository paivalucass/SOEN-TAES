def overlapping(list1, list2):
    '''Write a python function to check whether any value in a sequence exists in a sequence or not.'''
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Input parameters must be lists")
    if len(list1) == 0 or len(list2) == 0:
        return False 
    if set(list1) & set(list2):
        return True 
    else:
        return False 

    assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(overlapping([1,2,3,4,5],[6,7,8,9]), False)

if __name__ == '__main__':
    unittest.main()