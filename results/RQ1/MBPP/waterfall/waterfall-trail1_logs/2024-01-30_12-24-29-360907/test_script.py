def volume_sphere(r):
    import math
    try:
        radius = float(r)
        if radius <= 0:
            return "Invalid input"
        volume = (4/3) * math.pi * (radius**3)
        return round(volume, 3)
    except ValueError:
        return "Invalid input data"
    except OverflowError:
        return "Error: Input value too large"
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()