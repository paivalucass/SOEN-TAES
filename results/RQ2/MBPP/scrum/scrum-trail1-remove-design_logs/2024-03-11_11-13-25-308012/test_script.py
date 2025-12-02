def find_min_diff(arr, n):
    if len(arr) < 2:
        return "Array must have at least 2 elements"
    arr.sort()
    min_diff = float('inf')
    for i in range(n-1):
        if arr[i+1] - arr[i] < min_diff:
            min_diff = arr[i+1] - arr[i]
    return min_diff

assert find_min_diff([1,5,3,19,18,25], 6) == 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_min_diff([1,5,3,19,18,25],6), 1)

if __name__ == '__main__':
    unittest.main()