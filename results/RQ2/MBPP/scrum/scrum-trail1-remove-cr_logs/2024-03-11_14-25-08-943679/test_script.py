def count_rotation(arr):
    if len(arr) <= 1:
        return 0
    
    start = 0
    end = len(arr) - 1
    n = len(arr)
    
    while start <= end:
        mid = start + (end - start) // 2
        nextt = (mid + 1) % n
        prev = (mid + n - 1) % n
        
        if arr[mid] <= arr[nextt] and arr[mid] <= arr[prev]:
            return mid
        
        elif arr[start] <= arr[mid]:
            start = mid + 1
        
        elif arr[mid] <= arr[end]:
            end = mid - 1
    
    return 0  # default return if no rotation is required
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_rotation([3,2,1]), 1)

if __name__ == '__main__':
    unittest.main()