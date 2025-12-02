def count_nums(arr):
    count = 0
    for num in arr:
        num_str = str(abs(num))
        sum_of_digits = sum(int(digit) for digit in num_str)
        if sum_of_digits > 0:
            count += 1
    return count

import unittest

class Test(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(count_nums([]), 0)

    def test_negative_numbers(self):
        self.assertEqual(count_nums([-1, 11, -11]), 1)

    def test_positive_numbers(self):
        self.assertEqual(count_nums([1, 1, 2]), 3)

if __name__ == '__main__':
    unittest.main()