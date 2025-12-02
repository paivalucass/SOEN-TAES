def volume_cube(l):
    if not (isinstance(l, int) or isinstance(l, float)):
        return "Error: Invalid input data"
    if l <= 0:
        return "Error: Side length must be a positive number"
    return l ** 3
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(volume_cube(3), 27)

if __name__ == '__main__':
    unittest.main()