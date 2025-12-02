def count_nums(arr):
    count = 0
    for num in arr:
        num_str = str(abs(num))
        digit_sum = sum(int(digit) for digit in num_str)
        if digit_sum > 0:
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