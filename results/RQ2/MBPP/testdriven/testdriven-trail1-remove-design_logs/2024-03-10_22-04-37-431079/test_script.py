import math
import unittest

def otherside_rightangle(w, h):
    if w <= 0 or h <= 0:
        return "Both width and height must be positive numbers."
    return round(math.sqrt(w**2 + h**2), 15)

class Test(unittest.TestCase):
    def test_otherside_rightangle(self):
        self.assertEqual(otherside_rightangle(7, 8), 10.63014581273465)

if __name__ == '__main__':
    unittest.main()
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(otherside_rightangle(7, 8), 10.63014581273465)

if __name__ == '__main__':
    unittest.main()