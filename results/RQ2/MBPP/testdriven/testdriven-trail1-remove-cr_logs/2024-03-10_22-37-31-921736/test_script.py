def otherside_rightangle(w, h):
    if w <= 0 or h <= 0:
        raise ValueError("w and h must be positive numbers for a right-angled triangle.")
    
    third_side = (w**2 + h**2)**0.5
    
    return third_side
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(otherside_rightangle(7, 8), 10.63014581273465)

if __name__ == '__main__':
    unittest.main()