import math

def angle_complex(a, b):
    angle = math.atan2(b.imag, a.real)
    return angle
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(angle_complex(0,1j), 1.5707963267948966, places=6)

if __name__ == '__main__':
    unittest.main()