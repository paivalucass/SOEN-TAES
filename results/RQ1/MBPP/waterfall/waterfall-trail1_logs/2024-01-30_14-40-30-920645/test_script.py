def issort_list(list1):
    if not isinstance(list1, list):
        raise TypeError("Input is not a list")
    return list1 == sorted(list1) or list1 == sorted(list1, reverse=True)
import unittest

class Test(unittest.TestCase):
    def test_issort_list(self):
        self.assertTrue(issort_list([1,2,4,6,8,10,12,14,16,17]))

if __name__ == '__main__':
    unittest.main()