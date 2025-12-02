import math

def angle_complex(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Invalid Input"
    
    if a == 0 and b == 0:
        return 0
    
    angle = math.atan2(b, a)
    return angle
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(angle_complex(0,1j), 1.5707963267948966, places=3)

if __name__ == '__main__':
    unittest.main()