def count_rotation(arr):
    if not all(isinstance(x, int) for x in arr):
        return "Invalid input"
    
    n = len(arr)
    start = 0
    end = n - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        prev = (mid - 1 + n) % n
        next = (mid + 1) % n
        
        if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
            return mid
        
        elif arr[start] <= arr[mid]:
            start = mid + 1
            
        elif arr[mid] <= arr[end]:
            end = mid - 1
            
    return 0  # Default case for an already sorted array or empty array

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_rotation([3,2,1]), 1)

if __name__ == '__main__':
    unittest.main()