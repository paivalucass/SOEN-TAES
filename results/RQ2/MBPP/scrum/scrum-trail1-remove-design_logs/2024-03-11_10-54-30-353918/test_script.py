def polar_rect(x, y):
    import cmath
    rect = cmath.rect(x, y)
    polar = cmath.polar(rect)
    return polar, rect

import unittest

class Test(unittest.TestCase):
    def test_polar_rect(self):
        self.assertEqual(polar_rect(3, 4), ((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j)))

if __name__ == '__main__':
    unittest.main()