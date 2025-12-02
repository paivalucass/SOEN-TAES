def count_rotation(arr):
    n = len(arr)
    start = 0
    end = n - 1
    
    while start <= end:
        if arr[start] <= arr[end]:
            return start
        mid = (start + end) // 2
        next = (mid + 1) % n
        prev = (mid + n - 1) % n
        
        if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
            return mid
        elif arr[mid] <= arr[end]:
            end = mid - 1
        elif arr[mid] >= arr[start]:
            start = mid + 1
    return -1
import unittest

class Test(unittest.TestCase):
    def test_count_rotation(self):
        self.assertEqual(count_rotation([3,2,1]), 1)

if __name__ == '__main__':
    unittest.main()