import math

def triangle_area(r):
    if r < 0:
        return None
    else:
        s = (2 * r * math.sqrt(1 + r**2))
        area = 0.5 * r * s
        return area
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(1), math.pi / 2)
        self.assertEqual(triangle_area(2), 2 * math.pi)
        self.assertEqual(triangle_area(-1), None)

if __name__ == '__main__':
    unittest.main()