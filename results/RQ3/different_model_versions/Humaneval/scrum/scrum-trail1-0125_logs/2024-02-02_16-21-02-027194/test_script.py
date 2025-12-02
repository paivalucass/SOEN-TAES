def sort_array(array):
    if len(array) == 0:
        return []
    else:
        sorted_array = sorted(array)
        if (array[0] + array[-1]) % 2 == 0:
            return sorted_array[::-1]
        else:
            return sorted_array
import unittest

class Test(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(sort_array([]), [])

    def test_single_element_array(self):
        self.assertEqual(sort_array([5]), [5])

    def test_odd_sum_sorting(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])

    def test_even_sum_sorting(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])

if __name__ == '__main__':
    unittest.main()