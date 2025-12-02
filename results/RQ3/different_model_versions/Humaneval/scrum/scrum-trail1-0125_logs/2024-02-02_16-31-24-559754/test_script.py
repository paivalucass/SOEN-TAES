def is_simple_power(x, n):
    if x <= 0 or n <= 0:
        return "Error"
    if x == 1:
        return True
    if n == 1:
        return False
    
    power = 0
    while n**power < x:
        power += 1
    
    if n**power == x:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(is_simple_power(1, 4))
        self.assertTrue(is_simple_power(2, 2))
        self.assertTrue(is_simple_power(8, 2))
        self.assertFalse(is_simple_power(3, 2))
        self.assertFalse(is_simple_power(3, 1))
        self.assertFalse(is_simple_power(5, 3))

if __name__ == '__main__':
    unittest.main()