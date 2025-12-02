import math

def polar_rect(r, theta):
    if not isinstance(r, (int, float)) or not isinstance(theta, (int, float)):
        raise TypeError("r and theta must be numeric values")
    
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    
    if x == 0 and y == 0:
        raise ValueError("Invalid polar coordinates: r=0 and theta=0")

    return (x, y)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(polar_rect(3,4), ((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j)))

if __name__ == '__main__':
    unittest.main()