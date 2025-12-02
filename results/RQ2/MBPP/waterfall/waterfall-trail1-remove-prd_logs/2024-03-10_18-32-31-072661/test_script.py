import math

def convert(numbers):
    if isinstance(numbers, (int, float)):
        return (abs(numbers), 0)
    elif isinstance(numbers, complex):
        return (abs(numbers), math.phase(numbers))
    else:
        raise ValueError("Input must be a complex number")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(convert(1), (1.0, 0.0))

if __name__ == '__main__':
    unittest.main()