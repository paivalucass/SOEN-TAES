def max_Abs_Diff(arr):
    if arr is None or not isinstance(arr, (list, tuple)) or len(arr) < 2:
        return "Invalid Input"
    max_value = arr[0]
    min_value = arr[0]
    for num in arr:
        if not isinstance(num, (int, float)):
            return "Invalid Input"
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
    return abs(max_value - min_value)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_Abs_Diff((2,1,5,3)), 4)

if __name__ == '__main__':
    unittest.main()