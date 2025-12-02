import math

def lateralsurface_cylinder(r, h):
    return 2 * math.pi * r * h
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(lateralsuface_cylinder(10, 5), 314.15000000000003, delta=0.001)

if __name__ == '__main__':
    unittest.main()