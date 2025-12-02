def is_majority(arr, n, x):
    # Write your code here
    left = 0
    right = n - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == x:
            first_occurrence = mid
            right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    if first_occurrence is None:
        return False
    
    left = 0
    right = n - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == x:
            last_occurrence = mid
            left = mid + 1
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    if last_occurrence - first_occurrence + 1 > n // 2:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3), True)

if __name__ == '__main__':
    unittest.main()