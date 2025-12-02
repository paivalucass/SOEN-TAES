def sort_array(array):
    if array is None or len(array) == 0:
        return []

    sorted_array = array[:]
    if (sorted_array[0] + sorted_array[-1]) % 2 == 0:
        sorted_array.sort(reverse=True)
    else:
        sorted_array.sort()

    return sorted_array
import unittest

class Test(unittest.TestCase):
    def test_sort_array(self):
        self.assertEqual(sort_array([]), [])
        self.assertEqual(sort_array([5]), [5])
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])

if __name__ == '__main__':
    unittest.main()