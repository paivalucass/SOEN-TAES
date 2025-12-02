import math

def angle_complex(a, b):
    if not isinstance(a, (int, float, complex)) or not isinstance(b, (int, float, complex)):
        raise TypeError("a and b must be integers or floats")
    angle = math.atan2(b, a)
    return angle
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(angle_complex(0, 1j), 1.5707963267948966, places=3)

if __name__ == '__main__':
    unittest.main()