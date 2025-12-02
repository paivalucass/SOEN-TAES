def sum_of_digits(nums):
    if not isinstance(nums, list):
        raise TypeError("Input parameter 'nums' must be a list")

    if len(nums) == 0:
        raise ValueError("Input list cannot be empty")

    result = 0
    for num in nums:
        if not isinstance(num, (int, float)):
            raise TypeError("Input list must contain only numbers")

        num_str = str(abs(num))
        for digit in num_str:
            if digit.isdigit():
                result += int(digit)

    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_of_digits([10, 2, 56]), 14)

if __name__ == '__main__':
    unittest.main()