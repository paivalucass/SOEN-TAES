def specialFilter(nums):
    def isGreaterThanTen(num):
        return num > 10

    def isFirstAndLastDigitsOdd(num):
        str_num = str(num)
        return int(str_num[0]) % 2 != 0 and int(str_num[-1]) % 2 != 0

    count = 0
    for num in nums:
        if isGreaterThanTen(num) and isFirstAndLastDigitsOdd(num):
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)

if __name__ == '__main__':
    unittest.main()