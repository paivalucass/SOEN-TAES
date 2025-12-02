def convert(complex_number):
    # Step 1: Calculate the magnitude of the complex number (r) using the formula: r = abs(complex_number)
    r = abs(complex_number)
    
    # Step 2: Calculate the phase angle (theta) using the formula: theta = math.atan2(complex_number.imag, complex_number.real)
    import math
    theta = math.atan2(complex_number.imag, complex_number.real)
    
    # Step 3: Return the tuple (r, theta) representing the polar coordinates
    return (r, theta)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(convert(1), (1.0, 0.0))

if __name__ == '__main__':
    unittest.main()