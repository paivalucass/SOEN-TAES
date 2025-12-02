def count_nums(arr):
    def calculate_sum_of_digits(n):
        return sum(int(digit) for digit in str(abs(n)))

    count = 0
    for num in arr:
        num_str = str(num)
        if num < 0:
            num_str = num_str[1:]
        if calculate_sum_of_digits(num) > 0:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_count_nums_empty_array(self):
        self.assertEqual(count_nums([]), 0)

    def test_count_nums_negative_numbers(self):
        self.assertEqual(count_nums([-1, 11, -11]), 1)

    def test_count_nums_positive_numbers(self):
        self.assertEqual(count_nums([1, 1, 2]), 3)

if __name__ == '__main__':
    unittest.main()