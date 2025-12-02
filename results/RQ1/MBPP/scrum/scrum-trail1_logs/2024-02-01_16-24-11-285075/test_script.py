def get_median(arr1, arr2, n):
    arr = arr1 + arr2
    arr.sort()
    if n % 2 == 0:
        return (arr[n//2] + arr[n//2 - 1])/2
    else:
        return arr[n//2]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5), 16.0)

if __name__ == '__main__':
    unittest.main()