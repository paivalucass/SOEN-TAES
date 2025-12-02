def sum_of_digits(nums):
    try:
        total_sum = 0
        for num in nums:
            if not isinstance(num, int):
                raise TypeError("Input list should only contain integers")
            if num < 0:
                raise ValueError("Input list should not contain negative numbers")
            num_str = str(num)
            for digit in num_str:
                total_sum += int(digit)
        return total_sum
    except (TypeError, ValueError) as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_of_digits([10,2,56]), 14)

if __name__ == '__main__':
    unittest.main()