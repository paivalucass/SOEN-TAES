import cmath
import math

def polar_rect(r, theta):
    if r < 0:
        raise ValueError("Polar radius cannot be negative")

    x = r * math.cos(theta)
    y = r * math.sin(theta)
    rect_coords = (x, y)
    rect_complex = cmath.rect(r, theta)

    return rect_coords, rect_complex

# Test cases
assert polar_rect(3, 4) == ((3.0, 4.0), (-3.853489614486373-0.9364566872907963j))
assert polar_rect(0, 0) == ((0.0, 0.0), (0.0+0.0j))
assert polar_rect(-3, 4) == ((3.0, -0.0), (-3.0-0.0j))
assert polar_rect(1000000, 1000000) == ((-135314.58660130888, -989803.9399960116), (-1000000.0-0.0j))
assert polar_rect(1.7976931348623157e+308, 2.2250738585072014e-308) == ((1.7976931348623157e+308, 0.0), (0.0+2.2250738585072014e-308j))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(polar_rect(3, 4), ((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j)))

if __name__ == '__main__':
    unittest.main()