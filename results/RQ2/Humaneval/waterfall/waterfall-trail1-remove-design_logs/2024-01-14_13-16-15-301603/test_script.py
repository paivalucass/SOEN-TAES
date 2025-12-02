def count_nums(arr):
    def calculate_sum_of_digits(num):
        sum_of_digits = 0
        num_str = str(abs(num))
        for digit in num_str:
            sum_of_digits += int(digit)
        if num < 0:
            sum_of_digits *= -1
        return sum_of_digits

    count = 0
    for num in arr:
        sum_of_digits = calculate_sum_of_digits(num)
        if sum_of_digits > 0:
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