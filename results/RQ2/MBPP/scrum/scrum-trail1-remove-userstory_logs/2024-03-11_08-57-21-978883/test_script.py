def max_Abs_Diff(arr):
    if not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("Input array should contain only numbers")
    
    if len(arr) < 2:
        raise ValueError("Input array should have at least two elements")

    max_diff = max(arr) - min(arr)
    return abs(max_diff)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_Abs_Diff((2,1,5,3)), 4)

if __name__ == '__main__':
    unittest.main()