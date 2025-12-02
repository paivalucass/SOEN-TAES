def surfacearea_sphere(r):
    if type(r) != int and type(r) != float:
        return "Invalid Input"
    if r <= 0:
        return "Error: Please enter a positive radius"
    return 4 * math.pi * r**2
import unittest
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(surfacearea_sphere(10), 1256.6370614359173, delta=0.001)

if __name__ == '__main__':
    unittest.main()