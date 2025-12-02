def sum_of_digits(nums):
    total_sum = 0
    for num in nums:
        if not isinstance(num, int):
            raise ValueError("Invalid elements in the list")
        num_str = str(abs(num))
        for digit in num_str:
            total_sum += int(digit) * (-1 if num < 0 else 1)
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_of_digits([10,2,56]), 14)

if __name__ == '__main__':
    unittest.main()