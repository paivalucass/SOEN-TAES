def polar_rect(r, theta):
    import cmath
    x = r * cmath.cos(theta)
    y = r * cmath.sin(theta)
    return ((abs(x), abs(y)), (x + y * 1j))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(polar_rect(3, 4), ((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j)))

if __name__ == '__main__':
    unittest.main()