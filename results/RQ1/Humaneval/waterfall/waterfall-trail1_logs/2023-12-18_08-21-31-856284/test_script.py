def sort_array(array):
    sorted_array = array.copy()
    
    if not all(isinstance(x, int) and x >= 0 for x in sorted_array):
        return "Invalid input array"
    
    if len(sorted_array) == 0 or (len(sorted_array) == 1 and sum(sorted_array) == 0):
        return sorted_array

    sum_first_last = sorted_array[0] + sorted_array[-1]
    if sum_first_last % 2 == 0:
        return sorted(sorted_array, reverse=True)
    else:
        return sorted(sorted_array)
import unittest

class Test(unittest.TestCase):
    def test_sort_array(self):
        self.assertEqual(sort_array([]), [])
        self.assertEqual(sort_array([5]), [5])
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])

if __name__ == '__main__':
    unittest.main()