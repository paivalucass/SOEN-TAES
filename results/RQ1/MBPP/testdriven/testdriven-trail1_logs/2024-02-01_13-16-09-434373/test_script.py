def power_base_sum(base, power):
    '''Write a function that takes base and power as arguments and calculate the sum of all digits of the base to the specified power.'''
    result = base ** power
    return sum(int(i) for i in str(result))

assert power_base_sum(2, 100) == 115
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(power_base_sum(2, 100), 115)

if __name__ == '__main__':
    unittest.main()