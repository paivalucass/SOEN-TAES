def lateralsurface_cone(r, h):
    import math  # Move the import statement to the top of the script for better code organization
    # Calculate lateral surface area of the cone
    l = math.pi * r * math.sqrt(r**2 + h**2)
    return l
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(lateralsurface_cone(5,12), 204.20352248333654)

if __name__ == '__main__':
    unittest.main()