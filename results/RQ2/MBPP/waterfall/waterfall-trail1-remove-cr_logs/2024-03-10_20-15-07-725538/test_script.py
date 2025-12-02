import math

def lateralsurface_cone(r, h):
    LSA = math.pi * r * math.sqrt(r**2 + h**2)
    return LSA

print(lateralsurface_cone(3, 4))  # Expected output: 75.39822368615503
print(lateralsurface_cone(5, 7))  # Expected output: 164.9336148250681
print(lateralsurface_cone(5, 12))  # Expected output: 204.20352248333654
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(lateralsurface_cone(5, 12), 204.20352248333654)

if __name__ == '__main__':
    unittest.main()