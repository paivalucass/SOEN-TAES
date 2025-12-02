import math
def polar_rect(r, theta):
    x = round(r * math.cos(theta), 15)
    y = round(r * math.sin(theta), 15)
    z = complex(x, y)
    return (x, y), z
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(polar_rect(3, 4), ((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j)))

if __name__ == '__main__':
    unittest.main()