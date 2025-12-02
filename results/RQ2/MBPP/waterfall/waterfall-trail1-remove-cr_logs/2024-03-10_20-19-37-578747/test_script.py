def last(arr, x):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == x:
            result = mid
            left = mid + 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last([1,2,3], 1), 0)

if __name__ == '__main__':
    unittest.main()