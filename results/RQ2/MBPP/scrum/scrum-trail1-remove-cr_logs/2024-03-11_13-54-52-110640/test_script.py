def power_base_sum(base, power):
    if base < 0 or power < 0 or type(base) != int or type(power) != int:
        raise ValueError("Base and power must be non-negative integers")
        
    result = base ** power
    digit_sum = sum(int(digit) for digit in str(result))
    return digit_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(power_base_sum(2, 100), 115)

if __name__ == '__main__':
    unittest.main()