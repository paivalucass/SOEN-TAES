def count_rotation(arr):
    if len(arr) == 0:
        return 0
    
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        if arr[left] <= arr[right]:
            return left
        
        mid = (left + right) // 2
        next_index = (mid + 1) % len(arr)
        prev_index = (mid + len(arr) - 1) % len(arr)
        
        if arr[mid] <= arr[next_index] and arr[mid] <= arr[prev_index]:
            return mid
        elif arr[mid] <= arr[right]:
            right = mid - 1
        elif arr[mid] >= arr[left]:
            left = mid + 1
    
    return -1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_rotation([3,2,1]), 1)

if __name__ == '__main__':
    unittest.main()