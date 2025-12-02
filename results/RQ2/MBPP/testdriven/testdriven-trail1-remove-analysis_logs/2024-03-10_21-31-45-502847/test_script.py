def sum_of_digits(nums):
    sum_of_digits_list = []
    for num in nums:
        if isinstance(num, (int, float)):
            sum_digits = 0
            for digit in str(num):
                if digit.isdigit():
                    sum_digits += int(digit)
                else:
                    raise ValueError("Non-numeric input found")
            sum_of_digits_list.append(sum_digits)
        else:
            raise ValueError("Non-numeric input found")
    return sum_of_digits_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_of_digits([10, 2, 56]), 14)

if __name__ == '__main__':
    unittest.main()