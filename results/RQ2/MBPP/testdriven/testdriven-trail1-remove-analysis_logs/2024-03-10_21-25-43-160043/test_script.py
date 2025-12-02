import math

def triangle_area(r):
    if type(r) != int and type(r) != float:
        return None
    if r <= 0:
        return None
    else:
        base = (2 * r)
        height = r
        area = 0.5 * base * height
        return round(area, 2)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(triangle_area(3), (9 * math.pi) / 2)
        self.assertEqual(triangle_area(0), 0)
        self.assertEqual(triangle_area(-1), None)

if __name__ == '__main__':
    unittest.main()