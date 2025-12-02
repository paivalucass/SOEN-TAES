def count_rotation(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return 0
    else:
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            nextt = (mid + 1) % len(arr)
            prev = (mid + len(arr) - 1) % len(arr)
            if arr[mid] <= arr[nextt] and arr[mid] <= arr[prev]:
                return mid
            elif arr[start] <= arr[mid]:
                start = mid + 1
            elif arr[mid] <= arr[end]:
                end = mid - 1
        return -1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_rotation([3,2,1]), 1)

if __name__ == '__main__':
    unittest.main()