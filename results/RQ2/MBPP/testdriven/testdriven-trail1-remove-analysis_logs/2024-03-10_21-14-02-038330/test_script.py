def convert(numbers):
    if isinstance(numbers, complex):
        return cmath.polar(numbers)
    else:
        raise ValueError("Input must be a complex number")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(convert(1), (1.0, 0.0))

if __name__ == '__main__':
    unittest.main()