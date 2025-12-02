def smallest_change(arr):
    left = 0
    right = len(arr) - 1
    count = 0
    while left < right:
        if arr[left] != arr[right]:
            count += 1
        left += 1
        right -= 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_smallest_change(self):
        self.assertEqual(smallest_change([1,2,3,5,4,7,9,6]), 4)
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)

if __name__ == '__main__':
    unittest.main()