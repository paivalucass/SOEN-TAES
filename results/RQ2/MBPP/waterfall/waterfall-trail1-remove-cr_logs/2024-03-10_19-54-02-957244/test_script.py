import math

def angle_complex(a, b):
    if a == 0 and b == 0:
        return 0.0
    
    angle = math.atan2(b, a)
    
    return angle
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(angle_complex(0, 1j), 1.5707963267948966, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()