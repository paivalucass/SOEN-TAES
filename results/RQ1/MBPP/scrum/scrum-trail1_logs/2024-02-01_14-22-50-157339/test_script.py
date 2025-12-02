import math
def volume_sphere(r):
    if type(r) not in [int, float] or r <= 0:
        return "Invalid Input Error"
    else:
        return (4/3) * math.pi * r**3
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()