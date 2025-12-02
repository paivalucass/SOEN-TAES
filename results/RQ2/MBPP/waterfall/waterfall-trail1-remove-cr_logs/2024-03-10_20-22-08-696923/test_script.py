def count_rotation(arr):
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        if arr[low] <= arr[high]:
            return low

        mid = (low + high) // 2
        next_ = (mid + 1) % n
        prev = (mid + n - 1) % n

        if arr[mid] <= arr[next_] and arr[mid] <= arr[prev]:
            return mid
        elif arr[mid] <= arr[high]:
            high = mid - 1
        elif arr[mid] >= arr[low]:
            low = mid + 1

    return -1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_rotation([3,2,1]), 1)

if __name__ == '__main__':
    unittest.main()