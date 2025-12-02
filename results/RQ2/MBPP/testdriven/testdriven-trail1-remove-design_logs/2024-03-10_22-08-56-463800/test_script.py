def is_valid_input(n):
    if not isinstance(n, int) or n < 0 or n > 100:
        return False
    return True

def cal_sum(n): 
    if not is_valid_input(n):
        return "Error"
    if n == 0:
        return "Invalid input type error"
    
    a, b, c = 3, 0, 2
    for i in range(3, n + 1):
        a, b, c = b, c, a + b
    return a

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cal_sum(9), 49)

if __name__ == '__main__':
    unittest.main()