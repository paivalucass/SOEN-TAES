import math

def angle_complex(a, b):
    try:
        return math.atan2(b, a)
    except (ValueError, TypeError):
        return None if a != 0 else math.pi/2
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(angle_complex(0, 1j), 1.5707963267948966, places=6)

if __name__ == '__main__':
    unittest.main()