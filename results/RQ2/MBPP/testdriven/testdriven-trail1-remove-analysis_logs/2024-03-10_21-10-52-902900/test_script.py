import cmath

def angle_complex(a, b):
    angle_rad = cmath.phase(complex(a, b))
    return angle_rad

import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(angle_complex(0, 1j), 1.5707963267948966, places=3)

if __name__ == '__main__':
    unittest.main()