from typing import List

def count_rotation(arr: List[int]) -> int:
    if not arr or not all(isinstance(x, (int, float)) for x in arr):
        return "Input array is empty or contains non-numeric values"
    
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        if arr[low] <= arr[high]:
            return low
        
        mid = (low + high) // 2
        nextt = (mid + 1) % n
        prev = (mid + n - 1) % n

        if arr[mid] <= arr[nextt] and arr[mid] <= arr[prev]:
            return mid
        elif arr[mid] <= arr[high]:
            high = mid - 1
        elif arr[mid] >= arr[low]:
            low = mid + 1

    return 0
import unittest

class Test(unittest.TestCase):
    def test_count_rotation(self):
        self.assertEqual(count_rotation([3,2,1]), 1)

if __name__ == '__main__':
    unittest.main()