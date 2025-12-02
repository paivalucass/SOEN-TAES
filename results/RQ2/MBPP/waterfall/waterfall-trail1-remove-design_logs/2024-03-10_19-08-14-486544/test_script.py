def max_Abs_Diff(arr):
    if not arr:
        raise ValueError("Input array is empty")
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("Input array contains non-numeric values")
    
    return max(arr) - min(arr)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_Abs_Diff((2,1,5,3)), 4)

if __name__ == '__main__':
    unittest.main()