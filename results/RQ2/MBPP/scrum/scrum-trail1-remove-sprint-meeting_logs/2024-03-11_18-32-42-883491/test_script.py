def lateralsurface_cube(l):
    if type(l) != int and type(l) != float:
        return "Error: Input is not a number"
    elif l < 0:
        return "Error: Side length cannot be negative"
    else:
        return 4 * (l ** 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(lateralsurface_cube(5), 100)

if __name__ == '__main__':
    unittest.main()