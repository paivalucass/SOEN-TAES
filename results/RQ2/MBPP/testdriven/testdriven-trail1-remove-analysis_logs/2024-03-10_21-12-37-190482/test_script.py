def is_majority(arr, n, x):
    # Check if the input array is empty
    if not arr:
        return False
    
    # Find the first occurrence of x in the array
    start_index = 0
    end_index = n - 1

    # Binary search to find the first occurrence of x
    while start_index <= end_index:
        mid = (start_index + end_index) // 2
        if arr[mid] < x:
            start_index = mid + 1
        else:
            end_index = mid - 1
    
    # Check if x is the majority element
    if arr[start_index + n//2] == x:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3), True)

if __name__ == '__main__':
    unittest.main()