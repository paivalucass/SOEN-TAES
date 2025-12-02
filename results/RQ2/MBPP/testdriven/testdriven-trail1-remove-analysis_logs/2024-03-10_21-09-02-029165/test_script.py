def volume_sphere(r):
    import math
    if r <= 0:
        return "Radius should be a positive number"
    return (4/3) * math.pi * (r**3)
import math
import unittest

class TestVolumeSphere(unittest.TestCase):
    def test_volume_calculation(self):
        self.assertAlmostEqual(volume_sphere(10), 4188.790204786391, places=3)

if __name__ == '__main__':
    unittest.main()

# Output:
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK