def count_rotation(arr):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        next_index = (mid + 1) % n
        prev_index = (mid + n - 1) % n
        if arr[mid] <= arr[next_index] and arr[mid] <= arr[prev_index]:
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