def find_first_occurrence(array, target):
    left_index = 0
    right_index = len(array) - 1
    result = -1
    
    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2
        
        if array[mid_index] == target:
            result = mid_index
            right_index = mid_index - 1
        elif array[mid_index] < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_first_occurrence([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5), 1)

if __name__ == '__main__':
    unittest.main()