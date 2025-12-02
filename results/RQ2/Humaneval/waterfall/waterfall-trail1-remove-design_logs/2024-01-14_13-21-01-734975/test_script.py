def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            str_num = str(abs(num))
            first_digit = int(str_num[0])
            last_digit = int(str_num[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)

if __name__ == '__main__':
    unittest.main()