def count_nums(arr):
    if not arr or not all(isinstance(x, int) for x in arr):
        return 0
    
    def get_signed_digits(num):
        num_str = str(num)
        return [int(num_str[0] + digit) for digit in num_str[1:]] if num < 0 else [int(digit) for digit in num_str]
    
    def calculate_digit_sum(num):
        return sum(get_signed_digits(num))
    
    def count_elements_with_sum_greater_than_zero(nums):
        return sum(1 for num in nums if calculate_digit_sum(num) > 0)
    
    return count_elements_with_sum_greater_than_zero(arr)
import unittest

class Test(unittest.TestCase):
    def test_count_nums(self):
        self.assertEqual(count_nums([]), 0)
        self.assertEqual(count_nums([-1, 11, -11]), 1)
        self.assertEqual(count_nums([1, 1, 2]), 3)

if __name__ == '__main__':
    unittest.main()