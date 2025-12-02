def sort_array(array):
    if len(array) == 0:
        return []
    if (array[0] + array[-1]) % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)
import unittest

class Test(unittest.TestCase):
    def test_sort_array_odd_sum(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])

    def test_sort_array_even_sum(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])

    def test_sort_array_empty(self):
        self.assertEqual(sort_array([]), [])

    def test_sort_array_single_element(self):
        self.assertEqual(sort_array([5]), [5])

if __name__ == '__main__':
    unittest.main()