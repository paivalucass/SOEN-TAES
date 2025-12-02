def power(a, b):
    if type(a) != int or type(b) != int:
        return "Invalid Input"
    if b == 0:
        return 1
    elif b < 0:
        return 1 / power(a, -b)
    else:
        result = 1
        for _ in range(b):
            result *= a
        return result

import unittest

class Test(unittest.TestCase):
    def test_power_function(self):
        self.assertEqual(power(3, 4), 81)

if __name__ == '__main__':
    unittest.main()