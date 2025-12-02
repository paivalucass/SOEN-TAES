def volume_cylinder(r, h):
    import math
    return math.pi * (r ** 2) * h
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(volume_cylinder(10,5), 1570.7500000000002, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()