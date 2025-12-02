def get_median(arr1, arr2, n):
    arr = sorted(arr1 + arr2)
    if n % 2 == 0:
        median = (arr[n // 2 - 1] + arr[n // 2]) / 2
    else:
        median = arr[n // 2]
    return median
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5), 16.0)

if __name__ == '__main__':
    unittest.main()