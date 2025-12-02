def specialFilter(nums):
    def is_odd_digit(num):
        return str(num)[0] in ['1', '3', '5', '7', '9'] and str(num)[-1] in ['1', '3', '5', '7', '9']

    def count_special_numbers(nums):
        count = 0
        for num in nums:
            if num > 10 and is_odd_digit(num):
                count += 1
        return count

    return count_special_numbers(nums)
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
    
    def test2(self):
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)

if __name__ == '__main__':
    unittest.main()