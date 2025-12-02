def sum_of_digits(nums):
    if not isinstance(nums, list):
        raise ValueError("Input must be a list of numbers")

    result = []
    for num in nums:
        if not isinstance(num, int):
            raise ValueError("Input list must only contain numbers")

        digit_sum = 0
        num_str = str(num)
        for digit in num_str:
            if digit.isdigit():
                digit_sum += int(digit)
        result.append(digit_sum)

    return sum(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_of_digits([10, 2, 56]), 14)

if __name__ == '__main__':
    unittest.main()