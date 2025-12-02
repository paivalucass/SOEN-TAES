def polar_rect(r, theta):
    import cmath

    rect_coord = (r * cmath.cos(theta), r * cmath.sin(theta))
    polar_coord = (abs(r), cmath.phase(complex(theta)))

    return rect_coord, polar_coord
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(polar_rect(3, 4), ((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j)))

if __name__ == '__main__':
    unittest.main()