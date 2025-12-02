def search(arr):
    if not arr:
        return "Error message for empty input array"
    
    left_index = 0
    right_index = len(arr) - 1
    
    while left_index < right_index:
        mid_index = (left_index + right_index) // 2
        
        if mid_index % 2 == 1:
            mid_index -= 1
        
        if arr[mid_index] != arr[mid_index + 1]:
            right_index = mid_index
        else:
            left_index = mid_index + 2
    
    return arr[left_index]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(search([1,1,2,2,3]), 3)

if __name__ == '__main__':
    unittest.main()