def get_median(arr1, arr2, n):
    if len(arr1) != n or len(arr2) != n:
        return "Error: Input lists are not of the same size"
    merged_list = sorted(arr1 + arr2)
    mid = n // 2
    if n % 2 == 0:
        return (merged_list[mid - 1] + merged_list[mid]) / 2.0
    else:
        return float(merged_list[mid])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5), 16.0)

if __name__ == '__main__':
    unittest.main()