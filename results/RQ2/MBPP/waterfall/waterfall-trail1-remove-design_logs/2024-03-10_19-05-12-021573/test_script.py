def volume_sphere(r):
    import math
    
    if not isinstance(r, (int, float)) or r < 0:
        return "Error: Invalid input, radius must be a positive number"
    
    return round((4/3) * math.pi * (r**3), 14)
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(volume_sphere(10), 4188.790204786391, delta=0.001)

if __name__ == '__main__':
    unittest.main()