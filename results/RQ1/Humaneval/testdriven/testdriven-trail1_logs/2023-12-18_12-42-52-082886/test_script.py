def specialFilter(nums):
    def is_odd(num):
        return num % 2 != 0
    
    def is_valid(num):
        num_str = str(abs(num))
        return len(num_str) > 1 and is_odd(int(num_str[0])) and is_odd(int(num_str[-1])) and abs(num) > 10
    
    count = sum(1 for num in nums if isinstance(num, int) and is_valid(num))
    return count

import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(specialFilter([15, -73, 14, -15]), 1)
    
    def test2(self):
        self.assertEqual(specialFilter([33, -2, -3, 45, 21, 109]), 2)

if __name__ == '__main__':
    unittest.main()