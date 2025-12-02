def surfacearea_cube(l):
    if type(l) != int:
        return "Error: Input value must be a positive number"
    if l < 0:
        return "Error: Input value cannot be negative"
    if l == 0:
        return "Error: Input value cannot be zero"
    if l > 1000000:
        return "Error: Input size too large"
    return 6 * l * l
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(surfacearea_cube(5), 150)

if __name__ == '__main__':
    unittest.main()