def last(arr, x):
    if not arr:
        return -1
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right + 1) // 2
        if arr[mid] <= x:
            left = mid
        else:
            right = mid - 1
    if arr[left] == x:
        return left
    return -1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last([1,2,3], 1), 0)

if __name__ == '__main__':
    unittest.main()