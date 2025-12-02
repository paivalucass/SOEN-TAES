def max_Abs_Diff(arr):
    if len(arr) < 2:
        return "Error: Array should have at least two elements."
    else:
        max_value = max(arr)
        min_value = min(arr)
        return abs(max_value - min_value)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_Abs_Diff((2, 1, 5, 3)), 4)

if __name__ == '__main__':
    unittest.main()