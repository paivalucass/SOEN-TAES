def remove_kth_element(list1, k):
    if not list1 or k < 0 or k >= len(list1):
        return list1
    else:
        del list1[k-1]
        return list1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_kth_element([1,1,2,3,4,4,5,1], 3), [1, 1, 3, 4, 4, 5, 1])

if __name__ == '__main__':
    unittest.main()