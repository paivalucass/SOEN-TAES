def last(arr, target):
    if arr is None or len(arr) == 0:
        return -1

    left = 0
    right = len(arr) - 1
    last_index = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            last_index = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return last_index
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last([1,2,3], 1), 0)

if __name__ == '__main__':
    unittest.main()