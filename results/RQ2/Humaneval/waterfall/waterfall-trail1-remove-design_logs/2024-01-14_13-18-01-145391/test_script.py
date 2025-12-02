def add_elements(arr, k):
    total_sum = 0
    element_count = 0

    for num in arr[:k]:
        if isinstance(num, int) and 10 <= num <= 99:
            total_sum += num
            element_count += 1
        if element_count == 2:
            break

    return total_sum
import unittest

class Test(unittest.TestCase):
    def test_example(self):
        self.assertEqual(add_elements([111,21,3,4000,5,6,7,8,9], 4), 24)

    def test_empty_array(self):
        self.assertEqual(add_elements([], 0), 0)

    def test_single_element(self):
        self.assertEqual(add_elements([50], 1), 50)

    def test_all_elements_two_digits(self):
        self.assertEqual(add_elements([10, 20, 30, 40, 50], 5), 150)

    def test_k_greater_than_length(self):
        self.assertEqual(add_elements([10, 20, 30, 40, 50], 6), 150)

    def test_k_equals_length(self):
        self.assertEqual(add_elements([10, 20, 30, 40, 50], 5), 150)

if __name__ == '__main__':
    unittest.main()