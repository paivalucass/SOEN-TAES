def last(arr, x):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            result = mid
            left = mid + 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return result

# Test cases
assert last([], 5) == -1
assert last([5], 5) == 0
assert last([1, 2, 3, 4, 5, 5, 5, 6, 7], 5) == 6
assert last([1, 2, 3], 1) == 0
assert last([1, 2, 3], 4) == -1
assert last([1, 2, 2, 3], 2) == 2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last([1,2,3], 1), 0)

if __name__ == '__main__':
    unittest.main()