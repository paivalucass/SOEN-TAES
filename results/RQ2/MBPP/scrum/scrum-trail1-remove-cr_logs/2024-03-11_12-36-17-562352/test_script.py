def volume_sphere(r):
    import math
    try:
        assert type(r) in [int, float] and r >= 0, "Input must be a valid non-negative number"
        volume = (4/3) * math.pi * (r**3)
        return volume
    except AssertionError as e:
        if r < 0:
            return "Negative radius not allowed"
        else:
            return "Non-numeric input not allowed"
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()