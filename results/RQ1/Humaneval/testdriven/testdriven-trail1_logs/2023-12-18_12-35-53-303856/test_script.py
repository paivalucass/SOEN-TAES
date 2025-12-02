def count_nums(arr):
    count = 0
    for num in arr:
        if sum(int(digit) for digit in str(abs(num)) if digit != '-') > 0:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_count_nums_empty(self):
        self.assertEqual(count_nums([]), 0)

    def test_count_nums_negative_and_positive(self):
        self.assertEqual(count_nums([-1, 11, -11]), 1)

    def test_count_nums_all_positive(self):
        self.assertEqual(count_nums([1, 1, 2]), 3)

if __name__ == '__main__':
    unittest.main()