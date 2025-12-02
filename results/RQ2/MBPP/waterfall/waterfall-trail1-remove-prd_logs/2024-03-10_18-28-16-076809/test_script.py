def kth_element(arr, k):
    if len(arr) == 0:
        return "Error: Empty array"

    if k <= 0 or k > len(arr):
        return "Error: Invalid value of k"

    return arr[k-1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(kth_element([12,3,5,7,19], 2), 3)

if __name__ == '__main__':
    unittest.main()