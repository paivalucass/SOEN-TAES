def find_min_diff(arr, n):
    if len(arr) < 2:
        return None
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff if min_diff != float('inf') else None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_min_diff([1,5,3,19,18,25], 6), 1)

if __name__ == '__main__':
    unittest.main()