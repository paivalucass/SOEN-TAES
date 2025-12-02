import math

def angle_complex(a, b):
    if a == 0 and b == 0:
        return 0
    elif a == 0 and b.imag > 0:
        return math.pi / 2
    elif a == 0 and b.imag < 0:
        return -math.pi / 2
    else:
        return math.atan2(b.imag, a)

import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(angle_complex(0, 1j), 1.5707963267948966, places=3)

if __name__ == '__main__':
    unittest.main()