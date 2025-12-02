def convert(numbers):
    import math
    if isinstance(numbers, complex):
        r = abs(numbers)
        theta = math.atan2(numbers.imag, numbers.real)
        return (r, theta)
    elif isinstance(numbers, (int, float)):
        return (numbers, 0.0)
    else:
        raise ValueError("Input must be a complex number or a real number")

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(convert(1), (1.0, 0.0))

if __name__ == '__main__':
    unittest.main()