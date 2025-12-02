import cmath

def convert(numbers):
    if not isinstance(numbers, (int, float, complex)):
        raise ValueError("Input must be a complex number")
    
    magnitude = abs(numbers)
    angle = cmath.phase(numbers)
    
    return (magnitude, angle)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(convert(1), (1.0, 0.0))

if __name__ == '__main__':
    unittest.main()