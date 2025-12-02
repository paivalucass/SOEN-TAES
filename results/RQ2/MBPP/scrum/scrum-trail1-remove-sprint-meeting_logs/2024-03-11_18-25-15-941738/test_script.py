def max_Abs_Diff(arr):
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    max_element = max(arr)
    min_element = min(arr)
    
    return max_element - min_element
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_Abs_Diff((2,1,5,3)), 4)

if __name__ == '__main__':
    unittest.main()