def smallest_change(arr):
    start_index = 0
    end_index = len(arr) - 1
    changes_count = 0
    
    if arr is None or len(arr) == 0:
        return -1  # Error code for empty array
    
    while start_index <= end_index:
        if arr[start_index] != arr[end_index]:
            changes_count += 1
        start_index += 1
        end_index -= 1
    
    return changes_count
import unittest

class Test(unittest.TestCase):
    def test_smallest_change_1(self):
        self.assertEqual(smallest_change([1,2,3,5,4,7,9,6]), 4)

    def test_smallest_change_2(self):
        self.assertEqual(smallest_change([1, 2, 3, 4, 3, 2, 2]), 1)

    def test_smallest_change_3(self):
        self.assertEqual(smallest_change([1, 2, 3, 2, 1]), 0)

if __name__ == '__main__':
    unittest.main()