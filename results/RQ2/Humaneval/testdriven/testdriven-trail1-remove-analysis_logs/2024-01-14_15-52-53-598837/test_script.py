def sort_array(array):
    sorted_array = sorted(array, key=lambda x: x if (array[0] + array[-1]) % 2 else -x)
    return sorted_array
import unittest

class Test(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(function_under_test([]), [])

    def test_single_element_array(self):
        self.assertEqual(function_under_test([5]), [5])

    def test_odd_sum_array(self):
        self.assertEqual(function_under_test([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])

    def test_even_sum_array(self):
        self.assertEqual(function_under_test([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])

if __name__ == '__main__':
    unittest.main()