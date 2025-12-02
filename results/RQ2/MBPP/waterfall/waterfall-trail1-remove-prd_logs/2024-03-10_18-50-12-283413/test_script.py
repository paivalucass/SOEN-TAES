def count_rotation(arr):
    n = len(arr)
    low = 0
    high = n - 1
    
    while low <= high:
        if arr[low] <= arr[high]:
            return low
        
        mid = (low + high) // 2
        prev = (mid + n - 1) % n
        next = (mid + 1) % n
        
        if arr[mid] <= arr[prev] and arr[mid] <= arr[next]:
            return mid
        elif arr[mid] <= arr[high]:
            high = mid - 1
        elif arr[mid] >= arr[low]:
            low = mid + 1
    
    return -1

# Test Cases
assert count_rotation([4, 5, 6, 7, 0, 1, 2]) == 4
assert count_rotation([7, 0, 1, 2, 4, 5, 6]) == 1
assert count_rotation([1]) == 0
assert count_rotation([]) == -1
assert count_rotation([1,2,3]) == 0
assert count_rotation([3,1,2]) == 1
assert count_rotation([5,6,7,8,1,2,3,4]) == 4
assert count_rotation([3,3,3,3,3]) == 0
assert count_rotation([]) == -1
assert count_rotation([1]) == 0
# Add more test cases as needed
#assert count_rotation([1,2,3,...,1000]) == some value
#assert count_rotation('abc') == error
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_rotation([3,2,1]), 1)

if __name__ == '__main__':
    unittest.main()