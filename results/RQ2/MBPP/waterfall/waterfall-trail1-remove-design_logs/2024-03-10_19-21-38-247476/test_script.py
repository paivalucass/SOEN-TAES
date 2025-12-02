def remove_kth_element(list1, k):
    if len(list1) == 0 or k < 1 or k > len(list1) or not isinstance(k, int):
        return "Invalid input"
    else:
        del list1[k-1]
        return list1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_kth_element([1,1,2,3,4,4,5,1], 3), [1, 1, 3, 4, 4, 5, 1])

if __name__ == '__main__':
    unittest.main()