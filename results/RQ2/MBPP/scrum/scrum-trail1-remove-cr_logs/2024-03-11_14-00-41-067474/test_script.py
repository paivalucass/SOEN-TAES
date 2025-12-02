def find_min_diff(arr, n):
    arr.sort()
    diff = float('inf')
    for i in range(n-1):
        if arr[i+1] - arr[i] < diff:
            diff = arr[i+1] - arr[i]
    return diff
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_min_diff([1,5,3,19,18,25],6), 1)

if __name__ == '__main__':
    unittest.main()