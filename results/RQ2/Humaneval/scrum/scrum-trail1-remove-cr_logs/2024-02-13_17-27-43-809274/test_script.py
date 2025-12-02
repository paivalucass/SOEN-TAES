def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10 and is_first_last_digits_odd(num):
            count += 1
    return count

def is_first_last_digits_odd(num):
    num_str = str(abs(num))
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    if first_digit % 2 != 0 and last_digit % 2 != 0:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)

if __name__ == '__main__':
    unittest.main()