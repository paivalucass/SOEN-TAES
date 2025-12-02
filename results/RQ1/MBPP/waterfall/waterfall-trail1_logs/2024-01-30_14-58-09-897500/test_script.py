def power_base_sum(base, power):
    if base <= 0 or power <= 0:
        return "Error: Base or power cannot be negative or zero"
    
    result = base ** power
    
    digit_sum = 0
    while result > 0:
        digit_sum += result % 10
        result = result // 10
    
    return digit_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(power_base_sum(2, 100), 115)

if __name__ == '__main__':
    unittest.main()