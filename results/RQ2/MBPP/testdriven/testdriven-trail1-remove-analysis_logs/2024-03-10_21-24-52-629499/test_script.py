def remove_kth_element(list1, k):
    if not isinstance(list1, list) or not isinstance(k, int) or k < 0 or k >= len(list1):
        return "Invalid input"
    else:
        return list1[:k] + list1[k+1:]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_kth_element([1,1,2,3,4,4,5,1], 3), [1, 1, 3, 4, 4, 5, 1])

if __name__ == '__main__':
    unittest.main()