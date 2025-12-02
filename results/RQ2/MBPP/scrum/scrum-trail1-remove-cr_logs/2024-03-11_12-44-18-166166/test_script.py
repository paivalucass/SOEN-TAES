import math

def angle_complex(a, b):
    if not isinstance(a, complex) or not isinstance(b, complex):
        raise ValueError("Input parameters must be valid complex numbers")
    return math.atan2(b.imag, b.real)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(angle_complex(0, 1j), 1.5707963267948966, places=3)

if __name__ == '__main__':
    unittest.main()