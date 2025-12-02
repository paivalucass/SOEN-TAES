def round_and_sum(list1):
    def round_numbers(nums):
        return [round(num) for num in nums]

    def calculate_sum(nums):
        return sum(nums)

    rounded_list = round_numbers(list1)
    total_sum = calculate_sum(rounded_list)
    multiplied_sum = total_sum * len(list1)
    return round(multiplied_sum)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]), 243)

if __name__ == '__main__':
    unittest.main()