def sum_of_digits(nums):
    total_sum = 0
    for num in nums:
        total_sum += sum(int(digit) for digit in str(num))
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_of_digits([10, 2, 56]), 14)

if __name__ == '__main__':
    unittest.main()