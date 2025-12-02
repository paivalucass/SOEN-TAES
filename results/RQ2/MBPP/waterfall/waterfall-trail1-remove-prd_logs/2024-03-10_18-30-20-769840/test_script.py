def max_Abs_Diff(arr):
    if len(arr) < 2:
        return 0
    max_val = max(arr)
    min_val = min(arr)
    return abs(max_val - min_val)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_Abs_Diff((2,1,5,3)), 4)

if __name__ == '__main__':
    unittest.main()