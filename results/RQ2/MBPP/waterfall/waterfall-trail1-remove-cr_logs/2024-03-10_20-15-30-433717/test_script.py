def left_insertion(a, x):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left

# Test cases
assert left_insertion([1,2,4,5], 6) == 4
assert left_insertion([1,2,4,5], 0) == 0
assert left_insertion([1,2,4,5], 6) == 4
assert left_insertion([1,2,4,5], 3) == 2
import unittest

class Test(unittest.TestCase):
    def test_left_insertion(self):
        self.assertEqual(left_insertion([1,2,4,5], 6), 4)

if __name__ == '__main__':
    unittest.main()