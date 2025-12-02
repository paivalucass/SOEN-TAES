def find_min_diff(arr):
    if len(arr) < 2:
        return "Error: Input array should have at least 2 elements"
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr)-1):
        diff = abs(arr[i] - arr[i+1])
        if diff < min_diff:
            min_diff = diff 
    return min_diff
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_min_diff([1, 5, 3, 19, 18, 25]), 1)

if __name__ == '__main__':
    unittest.main()