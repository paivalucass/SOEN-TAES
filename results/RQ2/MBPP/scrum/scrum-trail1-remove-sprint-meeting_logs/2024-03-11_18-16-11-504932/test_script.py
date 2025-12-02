def surfacearea_sphere(r):
    if not isinstance(r, (int, float)):
        return "Error: Input value must be a number"
    if r == 0:
        return "Error: Zero radius input"
    if r < 0:
        return "Error: Negative radius input"
    if r > 10000:
        return "Error: Large radius input"
    
    import math
    surface_area = 4 * math.pi * r**2
    return surface_area
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(surfacearea_sphere(10), 1256.6370614359173, delta=0.001)

if __name__ == '__main__':
    unittest.main()