def polar_rect(x, y):
    import cmath
    real_part = x * cmath.cos(y)
    imag_part = x * cmath.sin(y)
    return (round(real_part, 10), round(imag_part, 10))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(polar_rect(3, 4), ((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j)))

if __name__ == '__main__':
    unittest.main()