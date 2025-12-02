def issort_list(list1):
    return list1 == sorted(list1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(issort_list([1,2,4,6,8,10,12,14,16,17]))

if __name__ == '__main__':
    unittest.main()