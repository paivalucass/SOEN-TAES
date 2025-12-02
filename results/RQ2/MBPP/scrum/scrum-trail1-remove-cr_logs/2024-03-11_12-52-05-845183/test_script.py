def is_majority(arr, n, x):
    if not arr == sorted(arr):
        raise ValueError("Input array is not sorted")
    if len(arr) != n:
        raise ValueError("Length parameter does not match the actual length of the array")
    
    count = arr.count(x)
    
    if count > n/2:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3), True)

if __name__ == '__main__':
    unittest.main()