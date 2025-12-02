import math

def angle_complex(a, b):
    if not isinstance(a, complex) or not isinstance(b, complex):
        raise ValueError("Input values must be valid complex numbers")
    angle = math.atan2(b.imag, a.real)
    return angle

import unittest
import math

class Test(unittest.TestCase):
    def test_angle_complex(self):
        self.assertAlmostEqual(angle_complex(0, 1j), 1.5707963267948966, delta=0.001)

if __name__ == '__main__':
    unittest.main()