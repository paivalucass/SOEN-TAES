def polar_rect(r, theta):
    import math
    if r < 0 or theta < 0 or theta > 2 * math.pi:
        return "Invalid Input Error"
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return (round(x, 10), round(y, 10))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(polar_rect(3, 4), ((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j)))

if __name__ == '__main__':
    unittest.main()