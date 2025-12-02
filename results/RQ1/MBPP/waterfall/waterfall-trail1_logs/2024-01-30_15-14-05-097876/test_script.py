def last(arr, x):
    if not arr:
        return -1  
    left_index = 0
    right_index = len(arr) - 1
    last_index = -1
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if arr[mid_index] == x:
            last_index = mid_index
            left_index = mid_index + 1
        elif arr[mid_index] < x:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return last_index
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last([1,2,3], 1), 0)

if __name__ == '__main__':
    unittest.main()