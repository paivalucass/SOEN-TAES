def kth_element(arr, k):
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        return "Error: Input array is not a list of integers"
    if k <= 0 or k > len(arr):
        return "Error: Invalid k value"
    return arr[k-1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(kth_element([12,3,5,7,19], 2), 3)

if __name__ == '__main__':
    unittest.main()