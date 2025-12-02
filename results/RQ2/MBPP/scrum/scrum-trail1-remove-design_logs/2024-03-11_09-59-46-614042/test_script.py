def volume_sphere(r):
    import math
    if r <= 0:
        raise ValueError("Error: Invalid input, radius must be a positive number")
    return (4/3) * math.pi * (r ** 3)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()