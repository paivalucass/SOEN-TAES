def issort_list(list1):
    '''Write a function to check whether a specified list is sorted or not.'''
    for i in range(len(list1)-1):
        if list1[i] > list1[i+1]:
            return False
    return True

assert issort_list([1,2,4,6,8,10,12,14,16,17])==True
import unittest

class Test(unittest.TestCase):
    def test_issort_list(self):
        self.assertTrue(issort_list([1,2,4,6,8,10,12,14,16,17]))

if __name__ == '__main__':
    unittest.main()