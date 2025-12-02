def count_rotation(arr):
    count = 0
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        if arr[low] <= arr[high]:
            return count

        mid = (low + high) // 2
        next = (mid + 1) % n
        prev = (mid + n - 1) % n

        if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
            return mid + 1

        if arr[mid] <= arr[high]:
            high = mid - 1
        if arr[mid] >= arr[low]:
            low = mid + 1

    return 0
# Test cases
assert count_rotation([3,2,1]) == 1
assert count_rotation([1,2,3,4,5]) == 0
assert count_rotation([4,5,6,1,2,3]) == 3
assert count_rotation([2]) == 0
assert count_rotation([]) == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_rotation([3,2,1]), 1)

if __name__ == '__main__':
    unittest.main()