def kth_element(arr, k):
    if not isinstance(arr, list):
        raise ValueError("Input array is not a valid list")
    
    if not isinstance(k, int):
        raise ValueError("Index k is not an integer")

    if not arr:
        raise ValueError("Input array is empty")

    if k < 1 or k > len(arr):
        raise ValueError("Index k is out of range")

    return arr[k-1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(kth_element([12,3,5,7,19], 2), 3)

if __name__ == '__main__':
    unittest.main()