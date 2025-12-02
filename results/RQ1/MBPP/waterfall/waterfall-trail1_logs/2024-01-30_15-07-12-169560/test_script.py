def find_min_diff(arr, n):
    if len(arr) < 2 or n != len(arr):
        return None

    arr.sort()
    min_diff = arr[1] - arr[0]
    for i in range(1, len(arr)-1):
        if arr[i+1] - arr[i] < min_diff:
            min_diff = arr[i+1] - arr[i]
    return min_diff
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_min_diff([1,5,3,19,18,25], 6), 1)

if __name__ == '__main__':
    unittest.main()