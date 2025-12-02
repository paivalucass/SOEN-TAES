import math
def polar_rect(r, theta):
    # Input validation
    if r < 0:
        raise ValueError("r should be non-negative")

    # Convert polar coordinates to rectangular coordinates
    x_rect = r * math.cos(theta)
    y_rect = r * math.sin(theta)

    return (x_rect, y_rect)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(polar_rect(3, 4), ((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j)))

if __name__ == '__main__':
    unittest.main()