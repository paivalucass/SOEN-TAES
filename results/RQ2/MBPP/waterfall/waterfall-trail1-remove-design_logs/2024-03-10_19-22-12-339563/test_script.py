def get_median(arr1, arr2, n):
    merged_arr = sorted(arr1 + arr2)
    mid = n // 2
    if n % 2 == 0:
        return (merged_arr[mid] + merged_arr[mid - 1]) / 2
    else:
        return merged_arr[mid]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5), 16.0)

if __name__ == '__main__':
    unittest.main()