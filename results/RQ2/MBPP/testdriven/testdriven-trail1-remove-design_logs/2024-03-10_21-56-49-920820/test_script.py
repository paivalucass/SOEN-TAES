def volume_sphere(r):
    if not isinstance(r, (int, float)) or r < 0:
        return "Error: Invalid input"
    return round((4/3) * math.pi * (r ** 3), 13)
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()