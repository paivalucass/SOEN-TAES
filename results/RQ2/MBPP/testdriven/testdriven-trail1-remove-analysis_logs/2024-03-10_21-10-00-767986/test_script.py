def kth_element(arr, k):
    if k == 0:
        return "Error: k should be greater than 0"
    if not arr:
        return "Error: Array is empty"
    if k < 1 or k > len(arr):
        return "Error: k is out of range"
    return arr[k-1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(kth_element([12,3,5,7,19], 2), 3)

if __name__ == '__main__':
    unittest.main()