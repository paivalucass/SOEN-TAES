def otherside_rightangle(w, h):
    import math
    if not isinstance(w, (int, float)) or not isinstance(h, (int, float)) or w < 0 or h < 0:
        raise ValueError("Input values must be non-negative numbers")

    return math.sqrt(w**2 + h**2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(otherside_rightangle(7, 8), 10.63014581273465)

if __name__ == '__main__':
    unittest.main()