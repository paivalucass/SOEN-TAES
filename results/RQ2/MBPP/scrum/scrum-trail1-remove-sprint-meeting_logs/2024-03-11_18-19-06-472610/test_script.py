def kth_element(arr, k):
    if not arr:
        raise ValueError("Input array should not be empty")
    
    if k < 1 or k > len(arr):
        raise ValueError("k is out of range")
    
    if k-1 not in range(len(arr)):
        raise ValueError("kth element not found in the array")
    
    return arr[k-1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(kth_element([12,3,5,7,19], 2), 3)

if __name__ == '__main__':
    unittest.main()